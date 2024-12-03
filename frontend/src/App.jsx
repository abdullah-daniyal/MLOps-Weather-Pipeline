import React, { useState } from 'react';
import AuthForm from './components/AuthForm';
import PredictionForm from './components/PredictionForm';

const App = () => {
    const [token, setToken] = useState(localStorage.getItem('token') || '');

    const handleSetToken = (newToken) => {
        setToken(newToken);
        localStorage.setItem('token', newToken);
    };

    const handleLogout = () => {
        setToken('');
        localStorage.removeItem('token');
    };

    return (
        <div style={{ padding: '20px' }}>
            {!token ? (
                <div>
                    <AuthForm isLogin={false} setToken={handleSetToken} />
                    <hr />
                    <AuthForm isLogin={true} setToken={handleSetToken} />
                </div>
            ) : (
                <div>
                    <button onClick={handleLogout}>Logout</button>
                    <PredictionForm token={token} />
                </div>
            )}
        </div>
    );
};

export default App;
