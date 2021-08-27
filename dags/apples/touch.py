from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='touch_apples',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['apples', 'touch'],
    params={"domain": "apples"},
    catchup=False,
) as dag:

    runme = BashOperator(
        task_id='touch_file_apples',
        bash_command='touch /tmp/airflow_touched_file_apples',
        do_xcom_push=False,
        queue='apples',
    )
    runme

if __name__ == "__main__":
    dag.cli()
