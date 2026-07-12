from datetime import datetime

from airflow import DAG
from airflow.providers.amazon.aws.operators.ecs import EcsRunTaskOperator

with DAG(
    dag_id="financial_platform_ecs_ingestion",
    description="Run the financial ingestion pipeline on ECS Fargate",
    start_date=datetime(2026, 7, 12),
    schedule=None,
    catchup=False,
    tags=["aws", "ecs", "fargate", "financial-data"],
) as dag:

    run_financial_ingestion = EcsRunTaskOperator(
        task_id="run_financial_ingestion",
        aws_conn_id=None,
        region_name="us-east-1",
        cluster="financial-platform-cluster",
        task_definition="financial-platform-task:1",
        launch_type="FARGATE",
        overrides={
            "containerOverrides": [
                {
                    "name": "financial-platform",
                }
            ]
        },
        network_configuration={
            "awsvpcConfiguration": {
                "subnets": [
                    "subnet-0c5d99ec8800cec7a",
                    "subnet-0b3f0a8f8d443dad6",
                    "subnet-09c857e4a107c46a1",
                    "subnet-0ff5da44fe0bd0ec6",
                    "subnet-06f7661c0113162ef",
                    "subnet-05b1632afcabe15d2",
                ],
                "securityGroups": [
                    "sg-08052eca4e381c86e",
                ],
                "assignPublicIp": "ENABLED",
            }
        },
        awslogs_group="/ecs/financial-platform",
        awslogs_region="us-east-1",
        awslogs_stream_prefix="ecs/financial-platform",
        container_name="financial-platform",
        wait_for_completion=True,
        reattach=False,
    )
