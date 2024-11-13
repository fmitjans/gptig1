import React from 'react';
import { Link } from 'react-router-dom';
import { FaHome } from 'react-icons/fa';
import 'bootstrap/dist/css/bootstrap.min.css';
import silueta from '../assets/logo-silueta2.png';  // Asegúrate de que la ruta sea correcta

const Navbar = () => {
  return (
    <nav
      className="navbar navbar-expand-lg navbar-light fixed-top"
      style={{
        backgroundImage: 'linear-gradient(90deg, #0061b6, #409ad6)',
        padding: '10px 20px',
        transition: 'background-color 1s ease', 
        boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
      }}
    >
      <div className="container-fluid d-flex justify-content-between align-items-center">
        {/* Link Home con ícono */}
        <div className="d-flex align-items-center">
          <FaHome style={{ marginRight: '10px', color: '#ffffff' ,fontSize: '1.5rem', verticalAlign: 'middle' }} />
          <Link to="/" className="navbar-brand" style={{ color: '#ffffff', fontWeight: 'bold', verticalAlign: 'middle' }}>
            Home
          </Link>
        </div>

        {/* Icono a la derecha */}
        <img
          src={silueta}
          alt="Logo"
          style={{ height: '40px', cursor: 'pointer' }}  // Ajusta el tamaño del ícono
        />
        
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
