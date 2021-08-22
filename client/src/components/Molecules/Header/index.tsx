import { Link } from "react-router-dom";
import "./index.scss";

const Header: React.FC = () => {
  return (
    <div className="header">
      <div className="logo">Circlism()</div>
      <nav>
        <Link to="/Venda">Soluctions</Link>

        <Link to="/Fidelize">Loyalize</Link>

        <Link to="/Planos">Plans</Link>

        <Link to="/Gerencie">manage</Link>

        <Link to="/Ajuda">Help</Link>

        <button>Login</button>
      </nav>
    </div>
  );
};

export default Header;
