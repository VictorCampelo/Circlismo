import { FormEvent, useContext, useState } from "react";
import "./index.scss";
import Header from "../../components/Molecules/Header";
import { Link, useHistory } from "react-router-dom";
import { AiFillGoogleCircle } from "react-icons/ai";
import { FiLock, FiMail } from 'react-icons/fi';
import { Input } from "../../components/Atoms/Input";

export function Login() {
  const history = useHistory();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState(false);

  const { signIn } = useContext(AuthContext);

  async function handleSignIn(e: FormEvent) {
    e.preventDefault();

    try {
      const res = await signIn({ email, password });

      console.log(res);

      history.push("/processImage");
    } catch (e) {
      console.log(e);
    }
  }

  return (
    <>
      <Header />
      <div>
        <form onSubmit={handleSignIn}>
          <div className="title">
            <h1>Login</h1>
          </div>

          <div className="inputContainer">
            <Input
              label="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              icon={<FiMail size={20} color="var(--black-800)" />}
            />

            <Input
              label="Senha"
              password
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              icon={<FiLock size={20} color="var(--black-800)" />}
            />
          </div>

          <Checkbox
            label="Lembrar usuário"
            confirm={confirm}
            toggleConfirm={() => setConfirm(!confirm)}
          />

          <div className="buttonContainer">
            <Button type="submit" title="ENTRAR" />
          </div>

          <div className="divisorContainer">
            <div className="divisor" />
            ou
            <div className="divisor" />
          </div>

          <div className="social">
            <AiFillGoogleCircle size={50} color="var(--gray-700)" />
            <FaFacebook size={50} color="var(--gray-700)" />
          </div>

          <div className="register">
            Não possui conta?
            <Link href="/register">
              <a> Cadastre-se!</a>
            </Link>
          </div>
        </form>
      </div>
    </>
  );
}

export default Login;
