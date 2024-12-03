import sys
import joblib
import os
import numpy as np
import pandas as pd

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'model.pkl')
    if not os.path.exists(model_path):
        print(f"Error: Model file not found at {model_path}")
        sys.exit(1)
    model = joblib.load(model_path)
    return model

def predict_temperature(humidity, wind_speed):
    model = load_model()
    # Use DataFrame with feature names to match training
    X = pd.DataFrame([[humidity, wind_speed]], columns=['Humidity', 'Wind Speed'])
    prediction = model.predict(X)
    return prediction[0]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid number of arguments. Usage: python predict.py <humidity> <wind_speed>")
        sys.exit(1)
    try:
        humidity = float(sys.argv[1])
        wind_speed = float(sys.argv[2])
        temp = predict_temperature(humidity, wind_speed)
        print(temp)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
