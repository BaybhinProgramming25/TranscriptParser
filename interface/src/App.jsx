import { BrowserRouter, Routes, Route  } from 'react-router-dom'
import { AuthProvider } from './context/AuthContext'

import Navbar from './components/Navbar/Navbar'
import Footer from './components/Footer/Footer'

import PublicRoute from './public-components/PublicRoute'
import Home from './public-components/Home/Home'
import ContactUs from './public-components/ContactUs/ContactUs'
import Login from './public-components/Login/Login'
import SignUp from './public-components/SignUp/SignUp'

import './App.css'
import Chat from './protected-components/Chat/Chat'

const App = () => {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Navbar />
          <Routes>
            <Route path="/" element={<Chat />}> </Route>
          </Routes>
        <Footer />
      </BrowserRouter>
    </AuthProvider> 
  )
}

export default App
