from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='touch_applesdev',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['applesdev', 'touch'],
    params={"domain": "applesdev"},
    catchup=False,
) as dag:

    runme = BashOperator(
        task_id='touch_file_applesdev',
        bash_command='touch /tmp/airflow_touched_file_applesdev',
        do_xcom_push=False,
        queue='applesdev',
    )
    runme

if __name__ == "__main__":
    dag.cli()
