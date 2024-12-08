FROM apache/airflow:2.5.1
USER airflow
RUN pip install scikit-learn pandas joblib requests mlflow pendulum==2.1.2
