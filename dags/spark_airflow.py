import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import date, datetime

dag = DAG(
    dag_id = "sparkflow",
    schedule_interval = "@daily",
    start_date=datetime.today()
)

start = PythonOperator(
    task_id="start",
    python_callable = lambda: print("Jobs started"),
    dag=dag
)

python_job = SparkSubmitOperator(
    task_id="python_job",
    conn_id="spark-conn",
    application="./utils/recreate.py",
    dag=dag
)


end = PythonOperator(
    task_id="end",
    python_callable = lambda: print("Jobs completed successfully"),
    dag=dag
)

start >> python_job >> end