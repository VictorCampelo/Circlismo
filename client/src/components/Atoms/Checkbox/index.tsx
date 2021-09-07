import { Container } from "./styles";
import { FaCheck } from 'react-icons/fa';
import { Link } from "react-router-dom";

interface CheckboxProps {
  confirm: boolean;
  toggleConfirm: () => void;
  label: string;
}

export const Checkbox = ({ confirm, toggleConfirm, label }: CheckboxProps) => {
  return (
    <Container 
      confirm={confirm}
    > 
      <div className="check">
        <button 
          type="button"
          id="btn" 
          className="btn" 
          onClick={() => toggleConfirm()} 
        >
          { confirm && <FaCheck  color="var(--gray-800)" />}
        </button>
        <label htmlFor="btn">{label}</label>
      </div>

      <Link to="/recover">
        Esqueceu sua senha
      </Link>
    </Container>
  )
}