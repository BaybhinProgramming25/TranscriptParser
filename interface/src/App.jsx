import { BrowserRouter, Routes, Route  } from 'react-router-dom'
import { AuthProvider } from './context/AuthContext'

import Navbar from './components/Navbar/Navbar'
import Footer from './components/Footer/Footer'

import PublicRoute from './public-components/PublicRoute'
import Home from './public-components/Home/Home'
import ContactUs from './public-components/ContactUs/ContactUs'
import Login from './public-components/Login/Login'
import SignUp from './public-components/SignUp/SignUp'
import EmailSent from './public-components/VerifySent/VerifyEmailSent'

import ProtectedRoute from './protected-components/ProtectedRoute'
import Chat from './protected-components/Chat'

import './App.css'

const App = () => {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Navbar />
          <Routes>

            <Route path="/" element={
              <PublicRoute>
                <Home />
              </PublicRoute>
            } />

            <Route path="/contact" element={
              <PublicRoute>
                <ContactUs />
              </PublicRoute>
            } />

            <Route path="/login" element={
              <PublicRoute>
                <Login />
              </PublicRoute>
            } />

            <Route path="/signup" element={
              <PublicRoute>
                <SignUp />
              </PublicRoute>
            } /> 

            <Route path="/verify-sent" element={
              <PublicRoute>
                <EmailSent />
              </PublicRoute>
            } />

            <Route path="/parse" element={
              <ProtectedRoute>
                <Chat />
              </ProtectedRoute>
            } />

          </Routes>
        <Footer />
      </BrowserRouter>
    </AuthProvider> 
  )
}

export default App
