import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './styles/App.css'
import { BrowserRouter } from 'react-router-dom'
import AppRoutes from './AppRoutes'
import Navbar from './components/Navbar';

function App() {
  return (
    <BrowserRouter>
          {/* Navbar siempre visible */}
          <Navbar />
      <AppRoutes />
    </BrowserRouter>
  )
}

export default App
