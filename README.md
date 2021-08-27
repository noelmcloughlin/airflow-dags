# Introduction
Apache-Airflow DAGs

# Scope
The scope is DAG's for Apache Airflow.

# Related project
See https://github.com/noelmcloughlin/airflow-component

# Description
This monorepo contains DAG's which could be used in any Airflow Deployment. The dags folder must be synchronized with the `dags/` folder on all particpating hosts using a file share or some 'sync_dags_from_repo' DAG.

# Rules
Do not write any code outside the tasks as it will be run every time Airflow parses the DAG 


# Included in this repo
- Example dags: https://github.com/apache/airflow/tree/main/airflow/example_dags
- Maintenance dags: https://github.com/teamclairvoyant/airflow-maintenance-dags


# Further reading

- About DAGs: https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html
- https://tech.scribd.com/blog/2020/breaking-up-the-dag-repo.html
- https://marclamberti.com/blog/variables-with-apache-airflow/
- https://www.linode.com/docs/guides/apache-airflow-tutorial-creating-connections-and-variables
- https://medium.com/apache-airflow/airflow-2-0-dag-authoring-redesigned-651edc397178
