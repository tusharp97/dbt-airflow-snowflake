# Define the default arguments for the DAG
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 21),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}
# Create the DAG with the specified schedule interval
dag = DAG('test_dbt_simple2_dag', default_args=default_args, schedule_interval=timedelta(days=1),catchup=False,)
# Define dbt tasks using BashOperator
task0 = BashOperator(
    task_id='dbt_task0',
    bash_command='pwd',
    dag=dag
)
task1 = BashOperator(
    task_id='dbt_task1',
    bash_command='dbt run  --project-dir /opt/airflow/dbt_snowflake --profiles-dir /opt/airflow/dbt_snowflake/profiles/',
    dag=dag
)
# Set task dependencies
task0>>task1 

