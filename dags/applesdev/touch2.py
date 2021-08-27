from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='touch_applesdev-worker02',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['applesdev-worker02', 'touch'],
    params={"domain": "applesdev-worker02"},
    catchup=False,
) as dag:

    runme = BashOperator(
        task_id='touch_file_applesdev-worker02',
        bash_command='touch /tmp/airflow_touched_file_applesdev-worker02',
        do_xcom_push=False,
        queue='applesdev-worker02',
    )
    runme

if __name__ == "__main__":
    dag.cli()
