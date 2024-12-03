import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os
import mlflow
import mlflow.sklearn
import numpy as np

def train():
    # Load processed data
    processed_data_path = 'data/processed_data.csv'
    df = pd.read_csv(processed_data_path)

    # Check for required columns
    required_columns = ['Humidity', 'Wind Speed', 'Temperature']
    if not all(col in df.columns for col in required_columns):
        print("Error: Missing required columns in the data.")
        return

    # Drop rows with missing values
    df = df.dropna(subset=required_columns)

    # Ensure there are enough samples
    if len(df) < 5:
        print("Error: Not enough samples to train the model.")
        return

    # Define features and target
    X = df[['Humidity', 'Wind Speed']]  # Predict Temperature based on Humidity and Wind Speed
    y = df['Temperature']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Check if test set has enough samples
    if len(X_test) < 2:
        print("Error: Not enough samples in the test set.")
        return

    # Start MLflow experiment
    mlflow.set_experiment("Weather_Prediction")

    with mlflow.start_run():
        # Log parameters
        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_param("features", ['Humidity', 'Wind Speed'])

        # Initialize and train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Evaluate the model
        score = model.score(X_test, y_test)
        print(f"Model R^2 Score: {score}")

        # Check if score is valid
        if np.isnan(score):
            print("Error: Model R^2 score is NaN.")
            return

        # Log metrics
        mlflow.log_metric("r2_score", score)

        # Save the model using MLflow
        os.makedirs('models', exist_ok=True)
        model_path = 'models/model.pkl'
        joblib.dump(model, model_path)
        print(f"Model saved to {model_path}")

        # Log the model artifact
        mlflow.log_artifact(model_path)

        # Register the model
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="sklearn-model",
            registered_model_name="WeatherPredictor"
        )

if __name__ == '__main__':
    train()
