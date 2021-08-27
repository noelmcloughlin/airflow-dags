from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='touch_apples-worker01',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['apples-worker01', 'touch'],
    params={"domain": "apples-worker01"},
    catchup=False,
) as dag:

    runme = BashOperator(
        task_id='touch_file_apples-worker01',
        bash_command='touch /tmp/airflow_touched_file_apples-worker01',
        do_xcom_push=False,
        queue='apples-worker01',
    )
    runme

if __name__ == "__main__":
    dag.cli()
