# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""DAG:BashOperator: Synchronize dags from remote repo
   Depends on airflow variables prefixed by dagid
"""

from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable
from airflow.utils.task_group import TaskGroup

args = {
    'owner': 'appsupport',
}

    # [START metadata]
with DAG(
    dag_id='synchronize_dags_from_repo',
    default_args=args,
                     # .------------- minute (0 - 59)
                     # | .---------- hour (0 - 23)
                     # | | .------- day of month (1 - 31)
                     # | | | .---- month (1 - 12) OR jan,feb,mar,apr ...
                     # | | | | .- weekday (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
                     # | | | | |
    schedule_interval='40 * * * *',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    tags=['scheduler', 'logs', 'housekeeping', 'ondemand'],
    catchup=False
) as dag:
    # [END metadata]

    domains = dag.dag_id + '__domains'
    repo = str(Variable.get("synchronize_dags_from_repo__repo"))

    # [START taskgroup]
    for domain in tuple(Variable.get(domains).split(',')):
        name = str(domain).strip()

        hosts = ('worker01','worker02')
        if domain == 'controller':
            hosts = ('primary', 'secondary')

        for host in hosts:
            queuename = name + '-' + host
            groupname = queuename + "_synchronize_dags"

            with TaskGroup(group_id=groupname) as tg:

                # [START tasks]
                clean = BashOperator(
                    task_id='clean',
                    queue=queuename,
                    bash_command='rm -fr ~/airflow-dags',
                    do_xcom_push=False,
                )

                clone = BashOperator(
                    task_id='clone',
                    queue=queuename,
                    bash_command='cd ~ && git clone ' + repo,
                    do_xcom_push=False,
                    env={
                        'HTTP_PROXY': "http://myproxy:8080",
                        'HTTPS_PROXY': "http://myproxy:8080",
                        'http_proxy': "http://myproxy:8080",
                        'https_proxy': "http://myproxy:8080",
                        'no_proxy': "localhost,*.net",
                    }
                )

                rsync = BashOperator(
                    task_id='rsync',
                    queue=queuename,
                    bash_command='rsync -Cavuzb --delete-after ~/airflow-dags/dags/* ~/dags',
                    do_xcom_push=False,
                )
                # [END tasks]
                clean >> clone >> rsync

            # [END taskgroup]
        # [END host]
    # [END domain]

if __name__ == "__main__":
    dag.cli()
