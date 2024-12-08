import requests
import pandas as pd
import os
from datetime import datetime, timedelta

API_KEY = '4e2eef88d2b44a9591974745242511'  
CITY = 'Islamabad'  
BASE_URL = 'http://api.weatherapi.com/v1'

def fetch_current_weather():
    """
    Fetches current weather data for the specified city.
    """
    url = f"{BASE_URL}/current.json"
    params = {
        'key': API_KEY,
        'q': CITY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'Temperature': data['current']['temp_c'],
            'Humidity': data['current']['humidity'],
            'Wind Speed': data['current']['wind_kph'],
            'Weather Condition': data['current']['condition']['text'],
            'Date': data['location']['localtime'].split(' ')[0],
            'Time': data['location']['localtime'].split(' ')[1]
        }
        return weather_data
    else:
        print(f"Failed to fetch current weather data: {response.status_code} - {response.text}")
        return None

def fetch_historical_weather(date):
    """
    Fetches historical weather data for the specified city and date.
    """
    url = f"{BASE_URL}/history.json"
    params = {
        'key': API_KEY,
        'q': CITY,
        'dt': date.strftime('%Y-%m-%d')
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        day_data = data['forecast']['forecastday'][0]['day']
        location_data = data['location']
        weather_data = {
            'Temperature': day_data['avgtemp_c'],
            'Humidity': day_data['avghumidity'],
            'Wind Speed': day_data['maxwind_kph'],
            'Weather Condition': day_data['condition']['text'],
            'Date': location_data['localtime'].split(' ')[0],
            'Time': location_data['localtime'].split(' ')[1]
        }
        return weather_data
    else:
        print(f"Failed to fetch historical weather data for {date.strftime('%Y-%m-%d')}: {response.status_code} - {response.text}")
        return None

def main():
    # Collect current weather data
    records = []
    current_weather = fetch_current_weather()
    if current_weather:
        records.append(current_weather)
    
    # Collect historical weather data for the past 30 days
    for i in range(1, 31):
        date = datetime.utcnow() - timedelta(days=i)
        historical_weather = fetch_historical_weather(date)
        if historical_weather:
            records.append(historical_weather)
    
    # Create DataFrame and save to CSV
    df = pd.DataFrame(records)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/raw_data.csv', index=False)
    print("Raw data saved to data/raw_data.csv")

if __name__ == '__main__':
    main()
