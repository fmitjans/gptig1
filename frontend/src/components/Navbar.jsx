import React from 'react';
import { Link } from 'react-router-dom';  // Para la navegación
import { FaHome } from 'react-icons/fa';  // Icono de casa
import 'bootstrap/dist/css/bootstrap.min.css';

const Navbar = () => {
  return (
    <nav
      className="navbar navbar-expand-lg navbar-light"
      style={{
        backgroundColor: '#f9c360',
        padding: '10px 20px',
        borderBottom: '2px solid #784532',
        boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
      }}
    >
      <div className="container-fluid">
        <Link to="/" className="navbar-brand" style={{ color: '#3d2822', fontWeight: 'bold' }}>
          <FaHome style={{ marginRight: '10px', fontSize: '1.5rem' }} />  {/* Ícono de Home */}
          Home
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
