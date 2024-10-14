from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import os

def load_data():
    os.system('python load_data.py')

def run_dbt():
    os.system('dbt run')

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 1)
}

with DAG('think_thrift_pipeline', default_args=default_args, schedule_interval='@daily') as dag:
    load_data_task = PythonOperator(task_id='load_data', python_callable=load_data)
    dbt_task = PythonOperator(task_id='run_dbt', python_callable=run_dbt)

    load_data_task >> dbt_task
