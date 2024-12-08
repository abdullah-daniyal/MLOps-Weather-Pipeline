import os
import pytest
from unittest.mock import patch
from dags.fetch_weather import fetch_current_weather, fetch_historical_weather

# Sample data to mock API responses
sample_current_weather = {
    'current': {
        'temp_c': 22.5,
        'humidity': 55,
        'wind_kph': 15.0,
        'condition': {'text': 'Partly cloudy'}
    },
    'location': {
        'localtime': '2024-04-01 14:00'
    }
}

sample_historical_weather = {
    'forecast': {
        'forecastday': [{
            'day': {
                'avgtemp_c': 20.0,
                'avghumidity': 60,
                'maxwind_kph': 18.0,
                'condition': {'text': 'Sunny'}
            }
        }]
    },
    'location': {
        'localtime': '2024-03-31 14:00'
    }
}

@patch('dags.fetch_weather.requests.get')
def test_fetch_current_weather(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = sample_current_weather

    weather_data = fetch_current_weather()
    assert weather_data is not None
    assert weather_data['Temperature'] == 22.5
    assert weather_data['Humidity'] == 55
    assert weather_data['Wind Speed'] == 15.0
    assert weather_data['Weather Condition'] == 'Partly cloudy'
    assert weather_data['Date'] == '2024-04-01'
    assert weather_data['Time'] == '14:00'

    mock_get.assert_called_once()

@patch('dags.fetch_weather.requests.get')
def test_fetch_historical_weather(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = sample_historical_weather

    from datetime import datetime
    test_date = datetime(2024, 3, 31)

    weather_data = fetch_historical_weather(test_date)
    assert weather_data is not None
    assert weather_data['Temperature'] == 20.0
    assert weather_data['Humidity'] == 60
    assert weather_data['Wind Speed'] == 18.0
    assert weather_data['Weather Condition'] == 'Sunny'
    assert weather_data['Date'] == '2024-03-31'
    assert weather_data['Time'] == '14:00'

    mock_get.assert_called_once()