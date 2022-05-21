from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

#defining DAG arguments
default_args = {
    'owner': 'Fadi Alsalti',
    'start_date': days_ago(0),
    'email': ['fadi.alsalti@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# define the DAG
dag = DAG(
    dag_id='process_web_log',
    default_args=default_args,
    description='Apache Airflow Assignment for Module 5',
    schedule_interval=timedelta(days=1),
)

# define the first task named extract_data
extract_data = BashOperator(
    task_id='extract_data',
    bash_command='''wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/accesslog.txt;
    cut -d" " -f1 accesslog.txt > extracted_data.txt''',
    dag=dag,
)

# define the sixth task named transform_data
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='grep -v 198.46.149.143 extracted_data.txt > transformed_data.txt',
    dag=dag,
)

# define the sixth task named load_data
load_data = BashOperator(
    task_id='load_data',
    bash_command='tar -czvf weblog.tar transformed_data.txt',
    dag=dag,
)

# task pipeline
extract_data >> transform_data >> load_data 