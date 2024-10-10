import { Route, Routes } from 'react-router-dom';
import Home from './views/Home';
import JobDetail from './views/JobDetail'; // Make sure the path matches your file structure

export default function AppRoutes() {
  return (
    <main>
      <Routes>
        <Route index element={<Home />} />
        <Route path="job/:id" element={<JobDetail />} /> {/* Route for job details */}
      </Routes>
    </main>
  );
}
