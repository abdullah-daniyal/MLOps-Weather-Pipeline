import os
import pandas as pd
import pytest
from dags.preprocess_data import preprocess

@pytest.fixture
def setup_test_data(tmp_path):
    """
    Fixture to set up the test environment by creating a temporary 'data/raw_data.csv' file.
    """
    # Define the data to be written to 'raw_data.csv'
    data = {
        "Temperature": [25.0, 30.0],
        "Humidity": [50.0, 60.0],
        "Wind Speed": [10.0, 12.0]
    }
    df = pd.DataFrame(data)
    
    # Create 'data/' directory within the temporary path
    data_dir = tmp_path / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    
    # Define the path for 'raw_data.csv'
    raw_data_path = data_dir / "raw_data.csv"
    
    # Write the DataFrame to 'raw_data.csv'
    df.to_csv(raw_data_path, index=False)
    
    # Change the current working directory to 'tmp_path'
    os.chdir(tmp_path)
    
    yield  # Test runs after this point
    
    # Teardown (optional, handled automatically by pytest's tmp_path)

def test_preprocess(setup_test_data):
    """
    Test the preprocess function to ensure it correctly processes raw_data.csv
    and outputs processed_data.csv with normalized values.
    """
    # Run the preprocess function
    preprocess()
    
    # Define the expected path for 'processed_data.csv'
    processed_data_path = "data/processed_data.csv"
    
    # Check if 'processed_data.csv' was created
    assert os.path.exists(processed_data_path), "Processed data file not created"
    
    # Load the processed data
    processed_df = pd.read_csv(processed_data_path)
    
    # Define the expected columns
    expected_columns = ["Temperature", "Humidity", "Wind Speed"]
    
    # Check if all expected columns are present
    assert all(col in processed_df.columns for col in expected_columns), "Missing expected columns in processed data"
    
    # Check if the numerical columns are normalized (mean approximately 0)
    for col in expected_columns:
        mean = processed_df[col].mean()
        assert abs(mean) < 1e-6, f"{col} not normalized properly"