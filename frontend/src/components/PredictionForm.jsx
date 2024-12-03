// frontend/src/components/PredictionForm.jsx

import React, { useState } from 'react';
import axios from 'axios';

const PredictionForm = ({ token }) => {
    const [humidity, setHumidity] = useState('');
    const [windSpeed, setWindSpeed] = useState('');
    const [prediction, setPrediction] = useState(null);

    const handlePredict = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(
                `${import.meta.env.VITE_API_URL}/predict`,
                {
                    humidity: parseFloat(humidity),
                    wind_speed: parseFloat(windSpeed),
                },
                {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                }
            );
            setPrediction(response.data.predicted_temperature);
        } catch (error) {
            console.error(error);
            alert(error.response?.data?.message || 'An error occurred');
        }
    };

    return (
        <div>
            <h2>Get Temperature Prediction</h2>
            <form onSubmit={handlePredict}>
                <input
                    type="number"
                    placeholder="Humidity"
                    value={humidity}
                    onChange={(e) => setHumidity(e.target.value)}
                    required
                />
                <input
                    type="number"
                    placeholder="Wind Speed"
                    value={windSpeed}
                    onChange={(e) => setWindSpeed(e.target.value)}
                    required
                />
                <button type="submit">Predict</button>
            </form>
            {prediction !== null && <p>Predicted Temperature: {prediction}°C</p>}
        </div>
    );
};

export default PredictionForm;
