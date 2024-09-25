import { Route, Routes } from 'react-router-dom'
import Home from './views/Home'

export default function AppRoutes() {
  return (
    <main>
      <Routes>
        <Route index element={<Home />} />
      </Routes>
    </main>
  );
}
