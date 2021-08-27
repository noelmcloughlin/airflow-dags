from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='touch_edge',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['edge', 'touch'],
    params={"domain": "edge"},
    catchup=False,
) as dag:

    runme = BashOperator(
        task_id='touch_file_edge',
        bash_command='touch /tmp/airflow_touched_file_edge',
        do_xcom_push=False,
        queue='edge',
    )
    runme

if __name__ == "__main__":
    dag.cli()
