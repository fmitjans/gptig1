//import React from 'react';
//import { useParams } from 'react-router-dom';

//export default function JobDetail() {
//  const { id } = useParams(); // Capture the job ID from the URL
//
//  return (
//    <div>
//      <h2>Job Detail - ID: {id}</h2>
//      {/* Add logic to fetch and display job details based on the ID */}
//    </div>
//  );
//}
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { FaBuilding, FaMapMarkerAlt, FaMoneyBillWave, FaClock, FaUserGraduate, FaClipboardCheck, FaBriefcase } from 'react-icons/fa';
import 'bootstrap/dist/css/bootstrap.min.css';

export default function JobDetails() {

  const [isLoading, setIsLoading] = useState(true);
  const [details, setDetails] = useState({});
  const [isEmailLoading, setIsEmailLoading] = useState(false);
  const [email, setEmail] = useState('');
  const [hasGeneratedEmail, setHasGeneratedEmail] = useState(false);

  const { id } = useParams();

  const loadDetails = () => {
    const backendUrl = import.meta.env.VITE_BACKEND_URL;
    fetch(`${backendUrl}/details?offer_id=${id}`)
    .then(response => response.json())
    .then(data => {
      console.log(data);
      setDetails(data);
    })
    .catch(error => console.error('Error:', error))
    .finally(() => {
      setIsLoading(false);
    });
  };

  useEffect(() => {
    if (details.empresa === undefined) {
      loadDetails();
    }
  }, []);

  // data['empresa']
  // data['actividad']
  // data['descripcion']
  // data['ubicacion']
  // data['remuneracion']
  // data['jornada'] 
  // data['nivel']   
  // data['experiencia']
  // data['contrato']
  // data['cargo']  
  // data['origen'] 
  // data['practica'] 

  let job = {
    titulo: 'Desarrollador Full Stack',
    empresa: 'Tech Solutions',
    actividadEconomica: 'Servicios de desarrollo de software',
    descripcion: {
      breve: 'Desarrollo de aplicaciones web y móviles, integración con APIs, mantenimiento de sistemas existentes, y colaboración con equipos de UX/UI.',
      ubicacion: 'Santiago, Chile',
      sueldo: 'CLP 1.800.000',
      jornada: 'Full time',
      fecha: '10 de octubre, 2024'
    },
    requisitos: {
      nivelEducacional: 'Educación universitaria completa',
      experiencia: '2 años de experiencia en desarrollo web'
    },
    caracteristicas: {
      tipoContrato: 'Indefinido',
      nivelCargo: 'Junior',
      origenOferta: 'LinkedIn',
      ofertaPractica: false
    }
  };

  const processedDetails = {
    titulo: details.titulo,
    actividadEconomica: details.actividad,
    descripcion: {
      breve: details.descripcion,
      ubicacion: details.ubicacion,
      sueldo: details.remuneracion,
      jornada: details.jornada,
      fecha: details.fecha
    },
    requisitos: {
      nivelEducacional: details.nivel,
      experiencia: details.experiencia
    },
    caracteristicas: {
      tipoContrato: details.contrato,
      nivelCargo: details.cargo,
      origenOferta: details.origen,
      ofertaPractica: details.practica
    }
  }

  job = {...job, ...processedDetails};

  const loadEmail = (details) => {
    console.log(details);
    let details_json = JSON.stringify(details);
    setIsEmailLoading(true);
    const backendUrl = import.meta.env.VITE_BACKEND_URL;
    fetch(`${backendUrl}/mail?details_json=${details_json}`)
    .then(response => response.json())
    .then(data => {
      console.log(data)
      setEmail(data.email);
    })
    .catch(error => console.error('Error:', error))
    .finally(() => {
      setIsEmailLoading(false);
      setHasGeneratedEmail(true);
    });
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  if (isLoading) {
    return (
      <div className="text-center">
        <div className="spinner"></div>
        <p>Cargando detalles...</p>
      </div>
    );
  } else {
  return (
    <>
  {/* clasificado 1: #E3EDF2*/}
    <div
  
      className="container my-5 p-5"
      style={{
        backgroundColor: '#E3EDF2',
        color: '#000', // Acá se puede cambiar el color de la letra
        border: '0px solid #000000',
        borderRadius: '5px',
        maxWidth: '900px',
        boxShadow: '0 12px 20px rgba(0, 0, 0, 0.5)',
      }}
    >
      {/* Título del trabajo */}
      <div
        style={{
          backgroundColor: '#0061b6',
          color: '#f9c360',
          padding: '20px',
          borderRadius: '7px',
          textAlign: 'center',
          marginBottom: '20px',
        }}
      >
        <h1 style={{ fontSize: '2.5rem', fontWeight: 'bold', color: '#FFFFFF' }}>
          {job.titulo}
        </h1>
      </div>

      {/* Botón para generar email de postulación */}
    {!(email || hasGeneratedEmail) && (
            <button
            style={{
              backgroundColor: '#0061b6',
              color: '#E3EDF2',
              padding: '20px',
              borderRadius: '7px',
              boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
              textAlign: 'center',
              marginTop: '15px',
              transition: 'transform 0.3s',
              border: '2px solid #000000',
              fontSize: '1.275rem',
            }}
            onMouseEnter={(e) => (e.currentTarget.style.transform = 'scale(1.03)')}
            onMouseLeave={(e) => (e.currentTarget.style.transform = 'scale(1)')}
            onClick={() => loadEmail(job)}
            disabled={isEmailLoading}
          >
            { isEmailLoading ?
            <div style={{ display: 'flex', alignItems: 'center' }}>
              <strong style={{ marginRight: '20px' }}>{'Generando email'}</strong>
              <div className="spinner2"></div>
            </div>
            :
            <strong>{'Generar email de postulación'}</strong>
          }
              
          </button>
    )}

    {/* Email generado */}
    {(email || hasGeneratedEmail) && (
      <div
        className="container my-5 p-5"
        style={{
          backgroundColor: '#E3EDF2',
          color: '#000',
          border: '0px solid ',
          borderRadius: '15px',
          maxWidth: '900px',
          height: '500px',
          boxShadow: '0 12px 20px rgba(0, 0, 0, 0)',
        }}
      >
        <div
          style={{
            backgroundColor: '#0061b6',
            color: '#000',
            padding: '20px',
            borderRadius: '15px',
            textAlign: 'center',
            marginBottom: '20px',
          }}
        >
          <h3 style={{ fontWeight: 'bold', color: '#FFFFFF' }}>
            Email de postulación
          </h3>
        </div>
        <textarea
          value={email}
          onChange={handleEmailChange}
          style={{
            padding: '10px',
            width: '100%',
            height: '80%',
            maxHeight: '80%',
            backgroundColor: '#fff',
            color: '#000',
            borderRadius: '10px',
            border: '2px solid #fff',
            outline: 'None',
            fontSize: '1.1rem',
          }}
        />
      </div>
    )}

      {/* Descripción larga del trabajo */}
      <div
        className="mb-4"
        style={{
          backgroundColor: '#fff',
          borderRadius: '10px',
          padding: '20px',
          border: '2px solid #fff',
          boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
          marginTop: '40px',
          marginBottom: '40px',
          color: '#000000',
        }}
      >
        <h4 style={{ fontWeight: 'bold', marginBottom: '15px', color: '#000' }}>Descripción</h4>
        <p style={{ lineHeight: '1.6', fontSize: '1.1rem' }}>
          {job.descripcion.breve}
        </p>
      </div>

      {/* Secciones de datos */}
      <div className="row">
        {/* Datos de contacto */}
        <div className="col-md-6 mb-4 d-flex">
          <div
            className="p-4 w-100"
            style={{
              backgroundColor: '#fff',
              borderRadius: '15px',
              border: '2px solid #fff',
              boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
              height: '100%',
              transition: 'transform 0.3s',
            }}
            onMouseEnter={(e) => (e.currentTarget.style.transform = 'scale(1.03)')}
            onMouseLeave={(e) => (e.currentTarget.style.transform = 'scale(1)')}
          >
            <h4 style={{ color: '#3d2822', fontWeight: 'bold', marginBottom: '20px',  color: '#000'  }}>
              <FaBuilding style={{ marginRight: '10px' }} />
              Empresa y Contacto
            </h4>
            <p><strong>Empresa:</strong> {job.empresa}</p>
            <p><strong>Actividad económica:</strong> {job.actividadEconomica}</p>
          </div>
        </div>

        {/* Descripción breve */}
        <div className="col-md-6 mb-4 d-flex">
          <div
            className="p-4 w-100"
            style={{
              backgroundColor: '#fff',
              borderRadius: '15px',
              border: '2px solid #fff',
              boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
              height: '100%',
              transition: 'transform 0.3s',
            }}
            onMouseEnter={(e) => (e.currentTarget.style.transform = 'scale(1.03)')}
            onMouseLeave={(e) => (e.currentTarget.style.transform = 'scale(1)')}
          >
            <h4 style={{fontWeight: 'bold', marginBottom: '20px',  color: '#000'  }}>
              <FaClipboardCheck style={{ marginRight: '10px' }} />
              Detalles importantes
            </h4>
            <p><FaMapMarkerAlt style={{ marginRight: '5px' }} /> {job.descripcion.ubicacion}</p>
            <p><FaMoneyBillWave style={{ marginRight: '5px' }} /> Sueldo: {job.descripcion.sueldo}</p>
            <p><FaClock style={{ marginRight: '5px' }} /> Jornada: {job.descripcion.jornada}</p>
            <p>Fecha de publicación: {job.descripcion.fecha}</p>
          </div>
        </div>
      </div>

      <div className="row">
        {/* Requisitos */}
        <div className="col-md-6 mb-4 d-flex">
          <div
            className="p-4 w-100"
            style={{
              backgroundColor: '#fff',
              borderRadius: '15px',
              border: '2px solid #fff',
              boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
              height: '100%',
              transition: 'transform 0.3s',
            }}
            onMouseEnter={(e) => (e.currentTarget.style.transform = 'scale(1.03)')}
            onMouseLeave={(e) => (e.currentTarget.style.transform = 'scale(1)')}
          >
            <h4 style={{fontWeight: 'bold', marginBottom: '20px',  color: '#000'  }}>
              <FaUserGraduate style={{ marginRight: '10px' }} />
              Requisitos
            </h4>
            <p><strong>Nivel educacional:</strong> {job.requisitos.nivelEducacional}</p>
            <p><strong>Experiencia:</strong> {job.requisitos.experiencia}</p>
          </div>
        </div>

        {/* Características */}
        <div className="col-md-6 mb-4 d-flex">
          <div
            className="p-4 w-100"
            style={{
              backgroundColor: '#fff',
              borderRadius: '15px',
              border: '2px solid #fff',
              boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
              height: '100%',
              transition: 'transform 0.3s',
            }}
            onMouseEnter={(e) => (e.currentTarget.style.transform = 'scale(1.03)')}
            onMouseLeave={(e) => (e.currentTarget.style.transform = 'scale(1)')}
          >
            <h4 style={{fontWeight: 'bold', marginBottom: '20px',  color: '#000'  }}>
              <FaBriefcase style={{ marginRight: '10px' }} />
              Características
            </h4>
            <p><strong>Tipo de contrato:</strong> {job.caracteristicas.tipoContrato}</p>
            <p><strong>Nivel del cargo:</strong> {job.caracteristicas.nivelCargo}</p>
            <p><strong>Origen de la oferta:</strong> {job.caracteristicas.origenOferta}</p>
            <p><strong>Oferta de práctica profesional:</strong> {job.caracteristicas.ofertaPractica ? 'Sí' : 'No'}</p>
          </div>
        </div>
      </div>

    </div>
    

  </>
  );
}
}
