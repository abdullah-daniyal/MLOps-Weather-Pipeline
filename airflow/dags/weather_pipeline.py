from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from fetch_weather import main as fetch_weather
from preprocess_data import preprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'weather_data_pipeline',
    default_args=default_args,
    description='A simple weather data pipeline',
    schedule_interval=timedelta(days=1),
)

collect_data = PythonOperator(
    task_id='collect_weather_data',
    python_callable=fetch_weather,
    dag=dag,
)

preprocess_data = PythonOperator(
    task_id='preprocess_weather_data',
    python_callable=preprocess,
    dag=dag,
)

collect_data >> preprocess_data
