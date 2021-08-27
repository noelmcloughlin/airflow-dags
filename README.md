# Introduction
DAGs for a federated reference deployment of Apache-Airflow

# Scope
Airflow-Component: https://github.com/noelmcloughlin/airflow-component

# Description
This monorepo contains DAG's which could be used in any Airflow Deployment.

The dags folder must be synchronized with the `dags/` folder on all particpating hosts using some mechanism.

# Rules
Do not write any code outside the tasks as it will be run every time Airflow parses the DAG 

# Further reading

- https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html
- https://github.com/apache/airflow/tree/main/airflow/example_dags
- https://tech.scribd.com/blog/2020/breaking-up-the-dag-repo.html
- https://marclamberti.com/blog/variables-with-apache-airflow/
- https://www.linode.com/docs/guides/apache-airflow-tutorial-creating-connections-and-variables
- https://medium.com/apache-airflow/airflow-2-0-dag-authoring-redesigned-651edc397178
- Maintenance dags: https://github.com/teamclairvoyant/airflow-maintenance-dags
