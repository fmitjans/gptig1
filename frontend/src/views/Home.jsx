import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import data from '../assets/regiones_comunas.json';
import logo from '../assets/logo.png';
import { Link } from 'react-router-dom';
import '../styles/App.css';


export default function Home() {
  const [searchKeyword, setSearchKeyword] = useState('');
  const [region, setRegion] = useState('');
  const [comuna, setComuna] = useState('');
  const [nivelEducativo, setNivelEducativo] = useState('');
  const [jornadaLaboral, setJornadaLaboral] = useState('');
  const [fechaPublicacion, setFechaPublicacion] = useState('');
  const [buttonText, setButtonText] = useState('Buscar');
  const [jobs, setJobs] = useState([{
    empresa: 'Empresa Ejemplo',
    region: 'Región Ejemplo',
    comuna: 'Comuna Ejemplo',
    nivelEducativo: 'Universitario',
    experiencia: '3 años',
    jornada: 'Full time',
    salario: 'CLP 1.500.000',
    cargo: 'Junior',
    titulo: 'Desarrollador Full Stack',
    descripcion: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus nec nunc ultricies ultricies. Nullam nec purus nec nunc ultricies ultricies.'
  }]);
  const [isLoading, setIsLoading] = useState(false); // Estado de carga añadido
  const [comunasPorRegion, setComunasPorRegion] = useState({});
  const [regiones, setRegiones] = useState([]);

  const nivelesEducativos = ['Sin educación formal', 'Educación básica incompleta', 'Educación básica completa', 
    'Educación media incompleta', 'Educación media completa', 'Educación técnica incompleta', 'Educación técnica completa', 
    'Educación universitaria incompleta', 'Educación universitaria completa', 'Magíster', 'Doctorado'];
  const jornadasLaborales = ['Full time', 'Part time'];
  const fechasPublicacion = ['', 'Hoy', 'Ayer', 'Menor a 3 días', 'Menor a 1 semana', 'Menor a 15 días', 'Menor a 1 mes', 'Menor a 2 meses'];

  useEffect(() => {
    setComunasPorRegion(JSON.parse(JSON.stringify(data)));
    setRegiones(Object.keys(data));
  }, []);

  const handleSearch = () => {
    const searchParams = {
      searchKeyword,
      region,
      comuna,
      nivelEducativo,
      jornadaLaboral,
      fechaPublicacion,
    };

    setButtonText('Buscando...');
    setIsLoading(true); // Iniciar el estado de carga al hacer la búsqueda

    fetch(`http://localhost:8000?keyword=${encodeURIComponent(searchKeyword)}`)
      .then(response => response.json())
      .then(data => {
        const renamedJobs = data.map(job => ({
          empresa: job.datosEmpresaOferta,
          descripcion: job.descripcionOferta,
          titulo: job.tituloOferta
        }));
        setJobs(renamedJobs);
      })
      .catch(error => {
        console.error('Error:', error);
      })
      .finally(() => {
        setIsLoading(false); // Terminar el estado de carga cuando la solicitud finalice
        setButtonText('Buscar');
      });

    console.log(searchParams);
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4">
        <img src={logo} alt="Jobsmatch Logo" style={{ maxWidth: '700px', height: 'auto' }} />
      </h1>


      {/* Search bar row */}
      <div className="row mb-3">
        <div className="col-md-10">
          <input
            type="text"
            className="form-control"
            placeholder="Profesión, empresa o palabra clave"
            value={searchKeyword}
            onChange={e => setSearchKeyword(e.target.value)}
          />
        </div>
        <div className="col-md-2">
          <button className="btn btn-primary w-100" onClick={handleSearch} disabled={isLoading} style={ {backgroundColor: '#f9c360', color: '#3d2822', borderColor:'#784532' }}>
            {buttonText}
          </button>
        </div>
      </div>

      {/* Filters form */}
      <div className="row mb-3">
        <div className="col-md-4">
          <select
            className="form-select"
            value={region}
            onChange={e => setRegion(e.target.value)}
            aria-label="Select Región"
          >
            <option value="">Región</option>
            {regiones.map((reg, index) => (
              <option key={index} value={reg}>
                {reg}
              </option>
            ))}
          </select>
        </div>
        <div className="col-md-4">
          <select
            className="form-select"
            value={comuna}
            onChange={e => setComuna(e.target.value)}
            aria-label="Select Comuna"
            disabled={!region}
          >
            <option value="">Comuna</option>
            {(comunasPorRegion[region] || []).map((com, index) => (
              <option key={index} value={com}>
                {com}
              </option>
            ))}
          </select>
        </div>
        <div className="col-md-4">
          <select
            className="form-select"
            value={nivelEducativo}
            onChange={e => setNivelEducativo(e.target.value)}
            aria-label="Select Nivel educativo"
          >
            <option value="">Nivel educativo</option>
            {nivelesEducativos.map((nivel, index) => (
              <option key={index} value={nivel}>
                {nivel}
              </option>
            ))}
          </select>
        </div>
      </div>

      <div className="row mb-3">
        <div className="col-md-4">
          <select
            className="form-select"
            value={jornadaLaboral}
            onChange={e => setJornadaLaboral(e.target.value)}
            aria-label="Select Jornada laboral"
          >
            <option value="">Jornada laboral</option>
            {jornadasLaborales.map((jornada, index) => (
              <option key={index} value={jornada}>
                {jornada}
              </option>
            ))}
          </select>
        </div>
        <div className="col-md-4">
          <select
            className="form-select"
            value={fechaPublicacion}
            onChange={e => setFechaPublicacion(e.target.value)}
            aria-label="Select Fecha de publicación"
          >
            <option value="">Fecha de publicación</option>
            {fechasPublicacion.slice(1).map((fecha, index) => (
              <option key={index} value={fecha}>
                {fecha}
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* Muestra el estado de carga */}
      {isLoading ? (
        <div className="text-center">
          <p>Cargando resultados...</p>
        </div>
      ) : (
        <div className="table-responsive mt-4">
          <table className="table table-bordered text-center">
            <thead className="table-light custom-table-header">
              <tr>
                <th>Titulo</th>
                <th>Empresa</th>
                <th>Descripcion</th>
              </tr>
            </thead>
            <tbody>
              {jobs.map((job, index) => (
                <tr key={index}>
                  <td>
                    <Link to={`/job/${index}`} style={{ textDecoration: 'none', color: '#007bff' }}>
                      {job.titulo}
                    </Link>
                  </td>
                  <td>{job.empresa}</td>
                  <td>{job.descripcion}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
