from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='touch_applestest',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['applestest', 'touch'],
    params={"domain": "applestest"},
    catchup=False,
) as dag:

    runme = BashOperator(
        task_id='touch_file_applestest',
        bash_command='touch /tmp/airflow_touched_file_applestest',
        do_xcom_push=False,
        queue='applestest',
    )
    runme

if __name__ == "__main__":
    dag.cli()
