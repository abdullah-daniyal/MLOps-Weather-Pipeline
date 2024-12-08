import os
import pandas as pd
import pytest
from unittest.mock import patch, MagicMock
from dags.train_model import train_model

# Sample processed data with a 'Target' column
sample_processed_data = {
    'Temperature': [0.0, 1.0],
    'Humidity': [-1.0, 0.0],
    'Wind Speed': [1.0, -1.0],
    'Target': [1, 0]
}

@pytest.fixture
def setup_test_data(tmp_path):
    # Create a temporary processed_data.csv for testing
    df = pd.DataFrame(sample_processed_data)
    processed_data_path = tmp_path / "processed_data.csv"
    df.to_csv(processed_data_path, index=False)
    # Change working directory to tmp_path for the duration of the test
    os.chdir(tmp_path)
    yield
    # Cleanup handled by tmp_path

@patch('dags.train_model.joblib.dump')
@patch('dags.train_model.joblib.load')
@patch('dags.train_model.train_test_split')
@patch('dags.train_model.YourModelClass')  # Replace with your actual model class
def test_train_model(mock_model_class, mock_train_test_split, mock_joblib_load, mock_joblib_dump, setup_test_data):
    # Mock train_test_split
    X = pd.DataFrame({
        'Temperature': [0.0, 1.0],
        'Humidity': [-1.0, 0.0],
        'Wind Speed': [1.0, -1.0]
    })
    y = pd.Series([1, 0])
    mock_train_test_split.return_value = (X, X, y, y)
    
    # Mock model instance
    mock_model = MagicMock()
    mock_model_class.return_value = mock_model
    mock_model.fit.return_value = mock_model
    mock_model.predict.return_value = [1, 0]
    
    # Run the train_model function
    train_model()
    
    # Assertions
    mock_train_test_split.assert_called_once()
    mock_model_class.assert_called_once()
    mock_model.fit.assert_called_once_with(X, y)
    mock_joblib_dump.assert_called_once_with(mock_model, 'model.joblib')