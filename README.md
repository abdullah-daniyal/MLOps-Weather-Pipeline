# MLOps Weather Prediction Pipeline

This repository implements a weather prediction pipeline using MLOps principles with tools like DVC, MLFlow, Airflow, Docker, Kubernetes, and CI/CD pipelines. The project aims to provide insights into the automation of data versioning, model training, and deployment processes.

## Project Overview

### Objectives:
1. Integrate DVC for managing datasets and machine learning models.
2. Use MLFlow for model versioning and tracking metrics.
3. Implement an automated pipeline using Airflow for data collection, preprocessing, and model training.
4. Set up Git-based workflows for development, testing, and production.
5. Deploy the model in a Kubernetes environment with Docker containers.

### Key Components:
- **Data Collection**: Weather data is fetched using an API and saved as CSV files.
- **Data Preprocessing**: The collected data is cleaned, normalized, and saved as processed data.
- **Model Training**: A linear regression model is trained to predict temperature based on features like humidity and wind speed.
- **Airflow Pipelines**: Automate the end-to-end process of fetching data, preprocessing, training models, and monitoring.
- **MLFlow Integration**: Track and version models, parameters, and metrics using MLFlow.
- **Docker & Kubernetes**: Containerize the application and deploy it on Kubernetes.
- **Git-based Branching Workflow**: Implement Git-based CI/CD pipelines for smooth development, testing, and production environments.

## Project Structure

```plaintext
mlops-weather-pipeline/
├── airflow/
│   ├── dags/
│   ├── logs/
│   └── plugins/
├── data/
│   ├── processed_data.csv.dvc
│   └── raw_data.csv
├── models/
│   └── model.pkl.dvc
├── .env
├── docker-compose.yml
├── dvc.yaml
├── fetch_weather.py
├── LICENSE
├── preprocess_data.py
├── README.md
└── train_model.py
```
Files Explanation:
fetch_weather.py: Fetches real-time and historical weather data from an API.
preprocess_data.py: Cleans and normalizes the weather data.
train_model.py: Trains a linear regression model using the processed data.
airflow/: Contains Airflow DAGs for automating the data pipeline.
dvc.yaml: Defines the DVC pipeline for versioning the datasets and models.
docker-compose.yml: Configures Docker containers for the application and Airflow.
models/model.pkl.dvc: The serialized model file managed by DVC.
Prerequisites
Before running the project, ensure you have the following:

Docker: For containerization and deployment.
Kubernetes: For managing containers in a distributed environment.
DVC: For versioning datasets and models.
MLFlow: For model versioning and logging.
Airflow: For automating workflows.
Python 3.8+: For running the scripts.

Installation
1. Set Up the Environment
Clone the repository:
git clone https://github.com/yourusername/mlops-weather-pipeline.git
cd mlops-weather-pipeline

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows

Install the dependencies:
pip install -r requirements.txt

2. Set Up Docker & Kubernetes
Use docker-compose.yml to set up Docker containers, including the Airflow setup.

Run Docker Compose to start the containers:
docker-compose up --build

3. DVC Setup
Initialize DVC for managing data and models:
dvc init

Push the data to DVC remote storage:
dvc push

4. Airflow Setup
Airflow is configured via Docker, and you can access the Airflow UI at http://localhost:8080. Make sure you have the appropriate DAGs and tasks set up for the data pipeline.

5. Running the Workflow
To trigger the workflow, either use Airflow's UI or manually run the following scripts:

fetch_weather.py: Fetches and saves raw weather data.
preprocess_data.py: Preprocesses the data.
train_model.py: Trains and saves the model.
6. Deploy the Model with Kubernetes
Use Minikube for local Kubernetes deployment. Set up the Kubernetes deployment configuration and deploy the application:
kubectl apply -f k8s/deployment.yaml

7. CI/CD Pipelines
Set up GitHub Actions for continuous integration and deployment:

Dev Branch: Active development.
Testing Branch: Runs automated tests and pushes Docker images.
Prod Branch: Deploys the application to Kubernetes.
Testing
Unit tests for the API and model can be found in the tests/ folder. Run tests using:
pytest

Conclusion
This project demonstrates a complete MLOps pipeline for weather prediction, with a focus on versioning, automation, and deployment. It integrates various tools like DVC, MLFlow, Airflow, Docker, and Kubernetes, following best practices for continuous integration and delivery.

License
This project is licensed under the MIT License. See the LICENSE file for details.
