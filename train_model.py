import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os

def train():
    # Load processed data
    processed_data_path = 'data/processed_data.csv'
    df = pd.read_csv(processed_data_path)

    # Define features and target
    X = df[['Humidity', 'Wind Speed']]  # Predict Temperature based on Humidity and Wind Speed
    y = df['Temperature']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model
    score = model.score(X_test, y_test)
    print(f"Model R^2 Score: {score}")

    # Save the model
    os.makedirs('models', exist_ok=True)
    model_path = 'models/model.pkl'
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == '__main__':
    train()
