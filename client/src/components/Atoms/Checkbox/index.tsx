import { Container } from "./styles";
import { FaCheck } from 'react-icons/fa';
import Link from 'next/link'

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

      <Link href="/recover">
        <a>Esqueceu sua senha</a>
      </Link>
    </Container>
  )
}