// frontend/src/components/AuthForm.jsx

import React, { useState } from 'react';
import axios from 'axios';

const AuthForm = ({ isLogin, setToken }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const endpoint = isLogin ? 'login' : 'signup';
        try {
            const response = await axios.post(`/api/auth/${endpoint}`, {
                username,
                password,
            });
            if (isLogin) {
                setToken(response.data.token);
            } else {
                alert(response.data.message);
            }
        } catch (error) {
            console.error(error);
            alert(error.response?.data?.message || 'An error occurred');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>{isLogin ? 'Login' : 'Sign Up'}</h2>
            <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
            />
            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
            />
            <button type="submit">{isLogin ? 'Login' : 'Sign Up'}</button>
        </form>
    );
};

export default AuthForm;
