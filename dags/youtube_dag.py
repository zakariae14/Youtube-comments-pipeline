from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, date
from youtube_etl import youtube_etl_fct

current_date = date.today()
current_year = current_date.year
current_month = current_date.month
current_day = current_date.day

start_date = datetime(current_year,current_month,current_day)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': start_date,
    'email': ['factorielle0122333333@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(days=1)
}

dag = DAG(
    'Youtube_dag',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='complete_Youtube_etl',
    python_callable=youtube_etl_fct,
    dag=dag,
)

run_etl