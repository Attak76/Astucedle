import './Login.css';
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { FaUser, FaLock, FaMoon, FaSun } from "react-icons/fa";

const Login = () => {
    const navigate = useNavigate();
    const handleLogin = (e) => {
        e.preventDefault();
        navigate("/dashboard");
      };

    const [isNightMode, setIsNightMode] = useState(false);

    const toggleNightMode = () => {
        setIsNightMode(!isNightMode);
        document.body.classList.toggle('night-mode', !isNightMode);
    };

    return (
        <div className='wrapper'>
            <form action=''>
                <h1>Connexion</h1>
                <div className='input-box'>
                    <input type='text' placeholder='Username' required />
                    <FaUser className="icon" />
                </div>
                <div className='input-box'>
                    <input type='password' placeholder='Password' required />
                    <FaLock className="icon" />
                </div>

                <div className='remember-forgot'>
                <div class="custom-checkbox-wrapper">
                    <input type="checkbox" id="custom-checkbox" />
                    <label for="custom-checkbox">Remember me</label>
                </div>
                    <a href='#'>Forgot Password?</a>
                </div>

                <button type='submit'>Login</button>

                <div className='register-link'>
                    <p>Don't have an account ? <a href='#'>Register</a></p>
                </div>
            </form>

            <div
                className="toggle-theme"
                onClick={toggleNightMode}
                style={{
                    position: "absolute",
                    top: "20px",
                    right: "20px",
                    cursor: "pointer",
                }}
            >
                {isNightMode ? <FaSun size={30} /> : <FaMoon size={30} />}
            </div>
        </div>
    );
};

export default Login;