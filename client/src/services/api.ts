import axios from 'axios';

export const api = axios.create({
  baseURL: 'http://localhost:3030'
})

interface SignUpProps {
  name: string;
  email: string;
  password: string;
  passwordConfirmation: string;
}

export async function signUp(user: SignUpProps) {
  return await api.post('auth/signup', user)
}