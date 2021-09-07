import { createContext, ReactNode, useEffect, useState } from "react";
import { setCookie, destroyCookie } from 'nookies';
import { useHistory } from "react-router-dom";
import { api } from "../services/api";
import { AxiosResponse } from "axios";

type SignInCredentials = {
  email: string;
  password: string;
}

type User = {
  email: string | null;
}

type AuthContextData = {
  signIn: (credentials: SignInCredentials) => Promise<AxiosResponse<any>>;
  SignOut: () => void;
  isAuthenticaded: boolean;
  user: User;
}

export const AuthContext = createContext({} as AuthContextData);

let authChannel: BroadcastChannel

type AuthProviderProps = {
  children: ReactNode;
}

export function SignOut() {
  const history = useHistory();

  destroyCookie(undefined, 'ultimo.auth.token');
  destroyCookie(undefined, 'ultimo.auth.refreshToken');

  authChannel.postMessage('SignOut')

  history.push('/')
}

export function AuthProvider({ children }: AuthProviderProps) {
  const [user, setUser] =  useState<User>({email: null});
  const isAuthenticaded = !!user;

  useEffect(() => {
    authChannel = new BroadcastChannel('auth');

    authChannel.onmessage = (message) => {
      switch(message.data){
        case 'singOut': 
          SignOut();
          break;
        default:
          break;
      }
    }
  }, [])

  // useEffect(() => {
  //   const { 'ultimo.auth.token': token } = parseCookies();

  //   if(token) {
  //     api.get('/me').then(res => {
  //       const { email } = res.data;
        
  //       setUser({ email })
  //     }).catch(() => {
  //       SignOut();
  //     })
  //   }
  // }, [])

  async function signIn({ email, password }: SignInCredentials) {
    const res = await api.post('/auth/signin', {
      email, 
      password 
    })

    const token = res.data.jwtToken;

    authChannel.postMessage('signIn')

    setCookie(undefined, 'ultimo.auth.token', token, {
      maxAge: 60 * 60 * 24 * 30, // 1 month
      path: '/',
      secure: true,
    });

    setUser({
      email,
    })

    api.defaults.headers['Authentication'] = `Bearer ${token}`

    return res
  }

  return (
    <AuthContext.Provider value={{ signIn, isAuthenticaded, user, SignOut }}>
      {children}
    </AuthContext.Provider>
  )
}