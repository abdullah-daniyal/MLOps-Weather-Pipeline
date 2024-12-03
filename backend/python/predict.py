import sys
import joblib
import os
import numpy as np

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')
    model = joblib.load(model_path)
    return model

def predict_temperature(humidity, wind_speed):
    model = load_model()
    X = np.array([[humidity, wind_speed]])
    prediction = model.predict(X)
    return prediction[0]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        sys.exit(1)
    try:
        humidity = float(sys.argv[1])
        wind_speed = float(sys.argv[2])
        temp = predict_temperature(humidity, wind_speed)
        print(temp)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
