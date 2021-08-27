from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='touch_orangestest',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['orangestest', 'touch'],
    params={"domain": "orangestest"},
    catchup=False,
) as dag:

    runme = BashOperator(
        task_id='touch_file_orangestest',
        bash_command='touch /tmp/airflow_touched_file_orangestest',
        do_xcom_push=False,
        queue='orangestest',
    )
    runme

if __name__ == "__main__":
    dag.cli()
