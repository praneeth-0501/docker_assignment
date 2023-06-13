from airflow.providers.postgres.operators.postgres import PostgresOperator
import airflow
from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id= 'postgres_dag',
    default_args=default_args,
    description='A simple DAG to connect to postgres',
    schedule_interval=timedelta(days=1),
)

task1 = PostgresOperator(
    sql= "sql/create_table.sql",
    task_id="createtable_task", 
    postgres_conn_id = "postgre_assign",
    dag=dag
)

task2 = PostgresOperator(
    sql="sql/insert_rows.sql",
    task_id="insert_rows_task", 
    postgres_conn_id = "postgre_assign",
    dag=dag
)

task3 = PostgresOperator(
    sql="sql/query.sql",
    task_id="query_task", 
    postgres_conn_id = "postgre_assign",
    dag=dag
)

task1 >> task2 >> task3

# https://www.projectpro.io/recipes/schedule-dag-file-create-table-and-load-data-into-it-mysql-and-hive-airflow#:~:text=Go%20to%20the%20admin%20tab,in%20Airflow%20to%20connect%20MySQL.