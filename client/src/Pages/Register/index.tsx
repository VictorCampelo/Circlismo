import { useState } from "react";
import { AiFillGoogleCircle } from "react-icons/ai";
import { FaFacebook } from "react-icons/fa";
import { FiMail, FiLock } from "react-icons/fi";
import { Link } from "react-router-dom";
import { Button } from "../../components/Atoms/Button";
import { Input } from "../../components/Atoms/Input";
import { Container } from "../../styles/preLogin";
import Header from "../../components/Molecules/Header";
import { signUp } from "../../services/api";


const Register = () => {
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const [passwordConfirmation, setPasswordConfirmation] = useState('');

  async function handleSignUp(e:React.MouseEvent<HTMLButtonElement, MouseEvent>) {
    e.preventDefault();

    try {
      const user = {
        email,
        name, 
        password,
        passwordConfirmation
      }

      const res = await signUp(user);

      console.log(res);
    } catch(e){
      console.log(e);
    }
  }

  return (
    <>
      <Header/>
      <Container>
        <form>
          <div className="title">
            <h1>Cadastro</h1>
          </div>

          <div className="inputContainer">
            <Input 
              label="Nome" 
              value={name}
              onChange={e => setName(e.target.value)}
              icon={<FiMail size={20} 
              color="var(--black-800)" />} 
            />

            <Input 
              label="Email" 
              value={email}
              onChange={e => setEmail(e.target.value)}
              icon={<FiMail size={20} 
              color="var(--black-800)" />} 
            />

            <Input 
              label="Senha" 
              value={password}
              onChange={e => setPassword(e.target.value)}
              password 
              icon={<FiLock size={20} color="var(--black-800)" />} 
            />
            
            <Input 
              label="Repetir senha" 
              password 
              value={passwordConfirmation}
              onChange={e => setPasswordConfirmation(e.target.value)}
              icon={<FiLock size={20} color="var(--black-800)" />} 
            />
          </div>
          
          <div className="buttonContainer">
            <Button onClick={handleSignUp} title="CONTINUAR" />
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
            Já possui conta?
            <Link to="/login">
              {' '}Faça seu login!
            </Link>
          </div>
        </form>
      </Container>
    </>
  );
};

export default Register;
