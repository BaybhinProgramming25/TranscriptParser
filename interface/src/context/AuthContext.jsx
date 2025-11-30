import { createContext, useContext, useState, useEffect } from 'react'
import axios from 'axios'

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {

    const [user, setUser] = useState(null);

    useEffect(() => {
        const loadUserToken = async () => {
            try {
                const response = await axios.post('http://localhost:3000/api/refresh', {}, { withCredentials: true });
                setUser(response.data.user_data);
            }
            catch (error) {
                console.error('Error with making axios post', error);
                alert("Token is no longer valid. Please login again");
            }
        } 
        loadUserToken();
    }, [])

    const login = (user_data) => { 
        setUser(user_data); 
    }

    const logout = () => { 
        setUser(null); 
    }

    return (
        <AuthContext.Provider value={{ user, login, logout }}>
            {children}
        </AuthContext.Provider>
    )
}

export const useAuth = () => useContext(AuthContext);