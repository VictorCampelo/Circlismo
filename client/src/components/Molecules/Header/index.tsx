import { Link } from "react-router-dom";
import "./index.scss";

const Header: React.FC = () => {
  return (
    <div className="header">
      <div className="logo">Circlism</div>
      <nav>
        <Link to="/Venda">Venda</Link>

        <Link to="/Fidelize">Fidelize</Link>

        <Link to="/Planos">Planos</Link>

        <Link to="/Gerencie">Gerencie</Link>

        <Link to="/Ajuda">Ajuda</Link>

        <button>Começar</button>
      </nav>
    </div>
  );
};

export default Header;
