# Define the default arguments for the DAG
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.models.param import Param

# Define the default arguments for the DAG
default_args = {
    'owner': 'tushar',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 21),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}
# Create the DAG with the specified schedule interval
dag = DAG('test_dbt_simple2_dag', default_args=default_args
    ,schedule_interval=timedelta(days=1),catchup=False,
   params={"my_int_param": Param(5, type="integer", minimum=3)},)
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

