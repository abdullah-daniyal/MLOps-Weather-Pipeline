# MLOps Weather Prediction Pipeline

This project is a full-fledged MLOps pipeline for weather prediction, leveraging various tools to manage datasets, model versioning, automation, and deployment. The pipeline is designed to fetch weather data, preprocess it, train a model, and then deploy the model through a complete CI/CD pipeline.

## Project Overview

The goal of this project is to provide students with hands-on experience in implementing MLOps practices using the following tools:

- **DVC (Data Version Control)**: For versioning datasets and machine learning models.
- **MLFlow**: For model versioning, logging, and management.
- **Airflow**: For automating workflows and managing data pipelines.
- **Docker**: For containerizing applications.
- **Kubernetes**: For deployment in a scalable, containerized environment.
- **Flask/FastAPI**: For building the REST API to serve predictions.

The project includes:
- Data collection from a weather API.
- Data preprocessing and feature engineering.
- Training a machine learning model for weather prediction.
- Integration with MLFlow for model versioning and tracking.
- Automating the workflow using Apache Airflow.
- Deployment of the full-stack application on Kubernetes using Docker.

## Prerequisites

Before you begin, ensure you have the following installed:

- Docker
- Docker Compose
- Python 3.8+
- Apache Airflow
- Minikube (for local Kubernetes cluster)
- Git

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

## Setup Instructions

### Step 1: Clone the Repository

First, clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/mlops-weather-pipeline.git
cd mlops-weather-pipeline
```

### Step 2: Install Dependencies

1. **Install Python dependencies**:
   
   Create a virtual environment and install the required libraries:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   pip install -r requirements.txt
   ```

2. **Install Docker**:
   Make sure Docker is running on your machine. You can install it from [Docker's official site](https://www.docker.com/).

3. **Install Apache Airflow**:
   If Airflow isn't installed already, you can install it using:

   ```bash
   pip install apache-airflow
   ```

4. **Install DVC**:

   DVC can be installed with pip:

   ```bash
   pip install dvc
   ```

### Step 3: Configure Environment Variables

Create a `.env` file in the project root with your API key and any necessary environment variables:

```env
API_KEY=your_weather_api_key
```

### Step 4: Run Data Collection Script

The `fetch_weather.py` script collects current and historical weather data, saving it as `raw_data.csv` in the `data/` folder.

Run the script with:

```bash
python fetch_weather.py
```

### Step 5: Preprocess Data

The `preprocess_data.py` script preprocesses the raw weather data by normalizing numerical values and handling missing data. It saves the processed data as `processed_data.csv`.

Run the script with:

```bash
python preprocess_data.py
```

### Step 6: Train the Model

The `train_model.py` script trains a Linear Regression model to predict temperature based on humidity and wind speed. It saves the trained model as `model.pkl`.

Run the script with:

```bash
python train_model.py
```

### Step 7: DVC Versioning

DVC is used for versioning the datasets and models. To set up DVC, initialize DVC and track the data files:

```bash
dvc init
dvc add data/raw_data.csv
dvc add data/processed_data.csv
dvc add models/model.pkl
git add .dvc .gitignore
git commit -m "Add data and model files"
```

### Step 8: Airflow Setup

Airflow is used to automate the data pipeline. You need to define Airflow DAGs to handle data collection, preprocessing, and model training.

1. **Define Airflow DAGs**:
   Create a DAG file in `airflow/dags/` for each of the steps, i.e., data collection, preprocessing, and model training.

2. **Run Airflow**:
   Start the Airflow web server and scheduler:

   ```bash
   airflow webserver -p 8080
   airflow scheduler
   ```

   Access the Airflow UI at `http://localhost:8080`.

### Step 9: Docker Setup

Docker is used to containerize the application. Use the `docker-compose.yml` file to set up the services.

```bash
docker-compose up --build
```

### Step 10: Kubernetes Deployment

Deploy the containerized application to Kubernetes. You can use Minikube for local deployment:

1. **Start Minikube**:

   ```bash
   minikube start
   ```

2. **Deploy the Application**:

   Apply Kubernetes deployment files:

   ```bash
   kubectl apply -f k8s/
   ```

3. **Access the Application**:
   Get the Minikube IP and access the service:

   ```bash
   minikube service <service-name> --url
   ```

### Step 11: CI/CD Setup

Use GitHub Actions or any CI/CD tool to automate the testing, building, and deployment process. This ensures that code changes trigger tests and deployments to the correct environments (Dev, Testing, and Production).

### Step 12: Write the Blog

In your Medium blog, document your MLOps workflow, the integration of tools like DVC, MLFlow, and Airflow, and the steps for automating model training and deployment.

### Step 13: Monitoring and Model Versioning with MLFlow

Integrate MLFlow to log models, metrics, and parameters. Use the model registry to manage different stages of the model (e.g., `staging`, `production`).

### Step 14: Run Tests

Ensure you have unit tests in place for your backend API (e.g., using `pytest` or `unittest`) to verify that predictions are working correctly.

```bash
pytest tests/test_api.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Conclusion

This project integrates various tools and practices essential for MLOps, such as data versioning with DVC, model management with MLFlow, and workflow automation with Airflow. It also demonstrates how to deploy a machine learning model to production using Docker and Kubernetes, making it a complete pipeline suitable for real-world applications.


