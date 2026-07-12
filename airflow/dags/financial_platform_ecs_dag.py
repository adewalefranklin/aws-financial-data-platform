from datetime import datetime

from airflow import DAG


with DAG(
    dag_id="financial_platform_ecs_ingestion",
    start_date=datetime(2026, 7, 12),
    schedule=None,
    catchup=False,
    tags=["aws", "ecs", "fargate", "financial-data"],
) as dag:
    pass