import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import data from '../assets/regiones_comunas.json';

export default function Home() {
  const [region, setRegion] = useState('');
  const [comuna, setComuna] = useState('');
  const [nivelEducativo, setNivelEducativo] = useState('');
  const [jornadaLaboral, setJornadaLaboral] = useState('');
  const [fechaPublicacion, setFechaPublicacion] = useState('');
  const [jobs, setJobs] = useState([{
    empresa: 'Empresa Ejemplo',
    region: 'Región Ejemplo',
    comuna: 'Comuna Ejemplo',
    nivelEducativo: 'Universitario',
    experiencia: '3 años',
    jornada: 'Full time',
    salario: 'CLP 1.500.000',
    cargo: 'Junior'
  }]);

  const [comunasPorRegion, setComunasPorRegion] = useState({});
  const [regiones, setRegiones] = useState([]);


  const nivelesEducativos = ['Sin educación formal', 'Educación básica incompleta', 'Educación básica completa', 'Educación media incompleta', 'Educación media completa', 'Educación técnica incompleta', 'Educación técnica completa', 'Educación universitaria incompleta', 'Educación universitaria completa', 'Magíster', 'Doctorado'];
  const jornadasLaborales = ['Full time', 'Part time'];

  useEffect(() => {
    setComunasPorRegion(JSON.parse(JSON.stringify(data)));
    setRegiones(Object.keys(data));
  }, []);

  const handleRegionChange = (e) => {
    const selectedRegion = e.target.value;
    setRegion(selectedRegion);
    setComuna([]);
  };

  const handleSearch = () => {
    const searchParams = {
      region,
      comuna,
      nivelEducativo,
      jornadaLaboral,
      fechaPublicacion,
    };

    axios.post('/backend/main.py', searchParams)
      .then(response => {
        setJobs(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the data!", error);
      });
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4">Jobsmatch</h1>
      
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
          <input
            type="date"
            className="form-control"
            value={fechaPublicacion}
            onChange={e => setFechaPublicacion(e.target.value)}
            placeholder="Fecha de publicación"
          />
        </div>
        <div className="col-md-4 d-flex align-items-center">
          <button className="btn btn-primary w-100" onClick={handleSearch}>
            Buscar
          </button>
        </div>
      </div>

      <div className="table-responsive mt-4">
        <table className="table table-bordered text-center">
          <thead className="table-light">
            <tr>
              <th>Empresa</th>
              <th>Región</th>
              <th>Ciudad/Comuna</th>
              <th>Nivel Educacional</th>
              <th>Años de Experiencia</th>
              <th>Jornada Laboral</th>
              <th>Salario</th>
              <th>Nivel de Cargo</th>
            </tr>
          </thead>
          <tbody>
            {jobs.map((job, index) => (
              <tr key={index}>
                <td>{job.empresa}</td>
                <td>{job.region}</td>
                <td>{job.comuna}</td>
                <td>{job.nivelEducativo}</td>
                <td>{job.experiencia}</td>
                <td>{job.jornada}</td>
                <td>{job.salario}</td>
                <td>{job.cargo}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}