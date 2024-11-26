import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def preprocess():
    # Load raw data
    raw_data_path = 'data/raw_data.csv'
    df = pd.read_csv(raw_data_path)

    # Handle missing values
    df = df.dropna()

    # Normalize numerical fields
    scaler = StandardScaler()
    df[['Temperature', 'Humidity', 'Wind Speed']] = scaler.fit_transform(df[['Temperature', 'Humidity', 'Wind Speed']])

    # Save processed data
    processed_data_path = 'data/processed_data.csv'
    df.to_csv(processed_data_path, index=False)
    print("Processed data saved to data/processed_data.csv")

if __name__ == '__main__':
    preprocess()
