# Cloud-Native Batch & Real-Time Financial Data Platform on AWS

![Python](https://img.shields.io/badge/Python-3.12-blue)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-EMR-red)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Apache Iceberg](https://img.shields.io/badge/Apache%20Iceberg-Lakehouse-2496ED)
![Amazon Athena](https://img.shields.io/badge/Amazon-Athena-FF9900)
![Amazon ECS](https://img.shields.io/badge/Amazon-ECS-green)
![Amazon Kinesis](https://img.shields.io/badge/Amazon-Kinesis-Streaming-purple)
![Apache Airflow](https://img.shields.io/badge/Apache-Airflow-red)
![Terraform](https://img.shields.io/badge/Terraform-IaC-623CE4)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-2088FF)

---

# Overview

This project demonstrates the design and implementation of a **cloud-native financial data platform** built entirely on AWS. The platform supports both **batch** and **real-time streaming** data ingestion while showcasing modern Data Engineering practices including distributed data processing, Lakehouse architecture, Infrastructure as Code, workflow orchestration, CI/CD and production monitoring.

Financial market data is collected from the **Finnhub API** using both REST and WebSocket interfaces.

Two independent ingestion pipelines were implemented:

- **Batch Pipeline** for scheduled market snapshots
- **Real-Time Streaming Pipeline** for continuous market events

The platform was intentionally built incrementally, beginning with local Python development before progressively integrating Docker, Amazon ECS, Amazon S3, Apache Spark, Amazon EMR, Apache Iceberg, AWS Glue, Amazon Athena, Amazon Kinesis, Apache Airflow, Terraform and GitHub Actions.

The objective was not simply to learn individual AWS services, but to understand how they integrate to form a production-ready cloud-native Data Engineering platform.

---

# Business Problem

Financial institutions receive market data from multiple external providers every second.

The platform must be capable of:

- Collecting historical market snapshots for reporting and analytics.
- Consuming real-time market events with minimal latency.
- Preserving raw data for replay and auditing.
- Transforming semi-structured JSON into analytical datasets.
- Validating data quality before consumption.
- Supporting both traditional Data Warehouse and modern Lakehouse architectures.
- Exposing curated datasets through SQL for downstream analytics.

Building such a platform requires multiple AWS services working together rather than relying on a single technology.

---

# Project Objectives

The primary objectives of this project were to:

- Build a modular Python ETL framework.
- Containerize the application using Docker.
- Deploy workloads using Amazon ECS with AWS Fargate.
- Store raw datasets inside Amazon S3.
- Process large datasets using Apache Spark on Amazon EMR.
- Implement production-style Data Quality Validation.
- Build an Apache Iceberg Lakehouse.
- Register metadata using AWS Glue Catalog.
- Query curated datasets with Amazon Athena.
- Build a real-time streaming pipeline using Amazon Kinesis.
- Implement workflow orchestration using Apache Airflow.
- Provision cloud infrastructure using Terraform.
- Automate testing using GitHub Actions.
- Implement operational monitoring using Amazon CloudWatch.

---

# Platform Capabilities

The completed platform demonstrates:

## Batch Processing

- REST API ingestion
- Containerized execution
- Scheduled processing
- Distributed Spark transformations
- Data validation
- Apache Iceberg Lakehouse
- SQL analytics with Athena

## Real-Time Streaming

- WebSocket ingestion
- Amazon Kinesis Data Streams
- Streaming producer and consumer
- Continuous event processing
- Bronze / Silver / Gold architecture

## Cloud Engineering

- Docker containerization
- Amazon ECS
- Amazon ECR
- IAM Roles
- Infrastructure as Code
- CI/CD
- Monitoring

---

# High-Level Architecture

```text
                        FINNHUB MARKET DATA
                 (REST API + WebSocket Streams)
                               │
               ┌───────────────┴────────────────┐
               │                                │
               ▼                                ▼
       Batch Processing                 Streaming Processing
               │                                │
               ▼                                ▼
          Amazon ECS                    Amazon Kinesis
         (Docker/Fargate)             Data Streams
               │                                │
               ▼                                ▼
           Amazon S3                    Streaming Consumer
               │                                │
               ▼                                ▼
      Apache Spark (EMR)          Bronze → Silver → Gold
               │
               ▼
     Data Quality Validation
               │
      ┌────────┴────────┐
      ▼                 ▼
Rejected Data      Valid Records
      │                 │
      ▼                 ▼
 Amazon S3       Apache Iceberg
                         │
                         ▼
                 AWS Glue Catalog
                         │
                         ▼
                  Amazon Athena
                         │
                         ▼
                 Business Analytics
```

---

# AWS Services Used

| Service | Purpose |
|----------|---------|
| Amazon ECS | Container orchestration |
| AWS Fargate | Serverless container execution |
| Amazon ECR | Docker image registry |
| Amazon S3 | Data Lake |
| Amazon EMR | Managed Apache Spark cluster |
| Apache Spark | Distributed ETL processing |
| Amazon Kinesis | Real-time data streaming |
| Apache Iceberg | Lakehouse storage |
| AWS Glue Catalog | Metadata management |
| Amazon Athena | SQL analytics |
| Amazon Redshift | Data warehouse implementation |
| Apache Airflow | Workflow orchestration |
| Terraform | Infrastructure as Code |
| GitHub Actions | Continuous Integration |
| Amazon CloudWatch | Monitoring & Logging |
| IAM | Secure authentication and authorization |

---

# Repository Structure

The project follows a modular, production-style structure where each directory has a clearly defined responsibility.

```text
aws-financial-data-platform/
│
├── .github/
│   └── workflows/
│       └── ci.yml                    # GitHub Actions CI pipeline
│
├── airflow/                          # Apache Airflow DAGs
│
├── docker/                           # Docker configuration
│
├── ecs/                              # Amazon ECS task configuration
│
├── emr_spark/                        # Apache Spark transformation scripts
│
├── kinesis/                          # Real-time streaming producer & consumer
│
├── redshift/                         # Amazon Redshift SQL scripts
│
├── screenshots/                      # Project screenshots
│
├── terraform/                        # Infrastructure as Code
│
├── tests/                            # Unit and integration tests
│
├── src/
│   └── project_pipeline/
│       ├── config.py
│       ├── extract.py
│       ├── load.py
│       ├── logger.py
│       └── pipeline.py
│
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
└── README.md
```

---

# Repository Design Philosophy

Rather than writing one large application, the project separates each responsibility into its own module.

This approach provides:

- Better maintainability
- Easier debugging
- Improved testing
- Reusable components
- Cleaner cloud deployments

Each AWS service is also responsible for one specific stage of the platform.

---

# Complete Platform Architecture

The platform consists of two independent ingestion pipelines that converge into analytical storage.

```text
                          FINNHUB MARKET DATA
                   REST API              WebSocket
                       │                     │
          ┌────────────┘                     └────────────┐
          │                                               │
          ▼                                               ▼
  Batch Processing                               Streaming Processing
          │                                               │
          ▼                                               ▼
 Python ETL Pipeline                           Python Producer
          │                                               │
          ▼                                               ▼
 Docker Container                           Amazon Kinesis Data Streams
          │                                               │
          ▼                                               ▼
 Amazon Elastic Container Registry          Python Consumer
          │                                               │
          ▼                                               ▼
 Amazon ECS (AWS Fargate)                 Amazon S3 Streaming Layer
          │                                               │
          ▼                                               ▼
 Amazon S3 Raw Landing Zone               Apache Spark Streaming
          │                                               │
          ▼                                               ▼
 Apache Spark (Amazon EMR)            Bronze → Silver → Gold
          │
          ▼
 Data Quality Validation
     │              │
     ▼              ▼
Rejected        Valid Records
Records             │
                    ▼
            Apache Iceberg
                    │
                    ▼
            AWS Glue Catalog
                    │
                    ▼
             Amazon Athena
                    │
                    ▼
            Business Analytics
```

---

# Platform Components

The platform is divided into logical layers.

## 1. Ingestion Layer

Responsible for collecting financial market data.

Technologies:

- Python
- Finnhub REST API
- Finnhub WebSocket
- Docker
- Amazon ECS
- Amazon Kinesis

Outputs:

- Raw JSON
- Streaming events

---

## 2. Storage Layer

Responsible for preserving raw and processed datasets.

Technologies:

- Amazon S3
- Apache Iceberg

Outputs:

- Raw Data Lake
- Curated Lakehouse

---

## 3. Processing Layer

Responsible for transforming raw data into analytical datasets.

Technologies:

- Amazon EMR
- Apache Spark

Tasks:

- Flatten nested JSON
- Generate timestamps
- Create partitions
- Validate records
- Remove duplicates

---

## 4. Metadata Layer

Responsible for making datasets discoverable.

Technology:

- AWS Glue Catalog

Stores:

- Database definitions
- Table definitions
- Column metadata
- Iceberg metadata

---

## 5. Analytics Layer

Responsible for querying curated datasets.

Technologies:

- Amazon Athena
- Amazon Redshift

Provides:

- SQL analytics
- Business reporting
- Ad hoc exploration

---

## 6. Orchestration Layer

Responsible for scheduling workloads.

Technology:

- Apache Airflow

Responsibilities:

- Trigger ECS Tasks
- Automate batch ingestion
- Coordinate pipeline execution

---

## 7. Infrastructure Layer

Responsible for provisioning cloud resources.

Technology:

- Terraform

Resources managed include:

- IAM
- S3
- ECS
- Networking
- Future infrastructure components

---

## 8. DevOps Layer

Responsible for automation.

Technology:

- GitHub Actions

Responsibilities:

- Install dependencies
- Execute tests
- Validate pull requests
- Prepare for automated deployment

---

# End-to-End Data Flow

The complete journey of a single stock quote is shown below.

```text
Finnhub

↓

Python ETL

↓

Docker

↓

Amazon ECR

↓

Amazon ECS

↓

Amazon S3 Raw

↓

Apache Spark (EMR)

↓

Data Quality Validation

↓

Apache Iceberg

↓

AWS Glue Catalog

↓

Amazon Athena

↓

Business Analytics
```

The streaming pipeline follows a parallel path.

```text
Finnhub WebSocket

↓

Python Producer

↓

Amazon Kinesis

↓

Python Consumer

↓

Amazon S3 Streaming

↓

Apache Spark Streaming

↓

Bronze

↓

Silver

↓

Gold
```

---

# Design Principles

The platform was built around several engineering principles.

- Build locally before deploying to AWS.
- Keep ingestion independent from transformation.
- Preserve raw data before processing.
- Validate data before analytics.
- Use managed AWS services where appropriate.
- Separate orchestration from execution.
- Build modular components that can evolve independently.
- Prefer Infrastructure as Code over manual provisioning.

---

# End-to-End Implementation Journey

Rather than building the entire platform at once, the project was implemented incrementally. Each stage was fully tested before introducing the next AWS service.

This mirrors how cloud-native data engineering platforms are typically developed in production.

---

# Stage 1 — Local Python Development

The project began as a modular Python ETL application developed locally.

Project modules:

```text
extract.py
load.py
pipeline.py
logger.py
config.py
main.py
```

Responsibilities:

| Module | Responsibility |
|---------|----------------|
| extract.py | Calls the Finnhub API |
| load.py | Uploads data to Amazon S3 |
| pipeline.py | Connects extraction and loading |
| logger.py | Application logging |
| config.py | Environment configuration |
| main.py | Entry point |

Why?

Building locally makes debugging significantly easier before introducing cloud infrastructure.

Output:

```text
Working ETL Application
```

↓

Next Stage

Docker

---

# Stage 2 — Docker Containerization

Once the application worked locally, it was containerized using Docker.

Docker packages:

- Python runtime
- Dependencies
- Source code
- Startup command

Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python","main.py"]
```

Why?

Docker guarantees that the application behaves identically on every machine.

Output

```text
Docker Image
```

↓

Next Stage

Amazon ECR

---

# Stage 3 — Amazon Elastic Container Registry (ECR)

The Docker image was pushed to Amazon ECR.

Workflow

```text
Docker Build

↓

Docker Image

↓

Amazon ECR
```

Why?

Amazon ECS cannot execute containers stored on a developer laptop.

ECR acts as the centralized image repository.

Output

```text
Container Image Available in AWS
```

↓

Next Stage

Amazon ECS

---

# Stage 4 — Amazon ECS using AWS Fargate

Amazon ECS executes the Docker container.

Configuration included:

- ECS Cluster
- Task Definition
- IAM Task Role
- IAM Execution Role
- CloudWatch Logging
- Networking

Execution Flow

```text
Amazon ECS

↓

Pull Docker Image

↓

Start Container

↓

Execute Python Pipeline

↓

Call Finnhub REST API

↓

Upload JSON to Amazon S3
```

Why ECS?

ECS removes the need to manually deploy Python applications to EC2 instances.

Why Fargate?

Fargate removes server management entirely.

Output

```text
Raw JSON Files in Amazon S3
```

↓

Next Stage

Amazon EMR

---

# Stage 5 — Amazon S3 Raw Landing Zone

Every API response is stored without modification.

Example

```text
raw/

    finnhub/

        quotes/

            year=2026/

                month=07/

                    day=13/

                        symbol=AAPL/
```

Why preserve raw data?

- Replay pipelines
- Debug transformations
- Historical archive
- Auditing
- Recovery

Raw data should never be overwritten.

↓

Next Stage

Apache Spark

---

# Stage 6 — Amazon EMR & Apache Spark

Amazon EMR provides the managed Spark cluster.

Apache Spark performs:

- Read JSON
- Flatten nested objects
- Convert timestamps
- Generate partitions
- Prepare analytical datasets

One important issue encountered:

Because the JSON files were written using

```python
json.dumps(..., indent=4)
```

Spark initially produced

```text
_corrupt_record
```

Solution

```python
.option("multiLine","true")
```

This allowed Spark to correctly parse the JSON.

Output

```text
Structured Spark DataFrame
```

↓

Next Stage

Data Quality Validation

---

# Stage 7 — Data Quality Validation

Before data enters the analytical layer every record is validated.

Validation Rules

✔ Symbol exists

✔ Current price exists

✔ Current price > 0

✔ Valid ingestion timestamp

✔ Valid market timestamp

✔ High ≥ Low

✔ Remove duplicates

Workflow

```text
Spark DataFrame

        │

        ▼

Data Quality Validation

        │

 ┌──────┴──────┐

 ▼             ▼

Rejected     Valid
```

Rejected records are stored separately inside Amazon S3.

Valid records continue into the Lakehouse.

↓

Next Stage

Apache Iceberg

---

# Stage 8 — Apache Iceberg Lakehouse

Validated data is written into Apache Iceberg.

Why Iceberg?

Compared to plain Parquet files, Iceberg provides:

- ACID transactions
- Snapshot history
- Schema evolution
- Hidden partitions
- Better metadata management

Warehouse

```text
Amazon S3

↓

iceberg/
```

Output

```text
Iceberg Table
```

↓

Next Stage

AWS Glue

---

# Stage 9 — AWS Glue Catalog

Spark automatically registers Iceberg tables inside AWS Glue.

Glue stores:

- Database
- Table
- Columns
- Data types
- Storage location

Example

```text
Database

financial_platform

↓

Table

quotes
```

Why?

Glue becomes the single metadata source used by Athena and other AWS services.

↓

Next Stage

Amazon Athena

---

# Stage 10 — Amazon Athena

Athena provides serverless SQL analytics.

Example

```sql
SELECT *

FROM financial_platform.quotes

LIMIT 10;
```

Execution

```text
Athena

↓

Glue Catalog

↓

Iceberg Metadata

↓

Amazon S3

↓

Query Results
```

No database server is required.

---

# Stage 11 — Real-Time Streaming Pipeline

The platform also supports continuous market event ingestion.

Architecture

```text
Finnhub WebSocket

↓

Python Producer

↓

Amazon Kinesis Data Streams

↓

Python Consumer

↓

Amazon S3 Streaming

↓

Apache Spark

↓

Bronze

↓

Silver

↓

Gold
```

Why Kinesis?

Unlike batch processing, Kinesis continuously ingests streaming market events with low latency.

This demonstrates both batch and streaming data engineering patterns within the same platform.

---

# Stage 12 — Airflow Orchestration

Apache Airflow orchestrates the ingestion pipeline.

Instead of executing Python directly, Airflow triggers the existing ECS task.

Workflow

```text
Airflow DAG

↓

Amazon ECS

↓

Docker Container

↓

Python Pipeline
```

This cleanly separates scheduling from execution.

---

# Stage 13 — Infrastructure as Code

Terraform is used to provision AWS infrastructure.

Managed resources include:

- Amazon S3
- IAM
- ECS
- Networking

Benefits

- Repeatable deployments
- Version-controlled infrastructure
- Easier environment recreation

---

# Stage 14 — CI/CD

GitHub Actions automates testing.

Workflow

```text
Git Push

↓

GitHub Actions

↓

Install Dependencies

↓

Run Pytest

↓

Report Results
```

This ensures new changes do not break existing functionality.

---

# Stage 15 — Monitoring

Amazon CloudWatch provides operational visibility.

Current monitoring includes:

- ECS Logs
- Application Logs
- EMR Job Monitoring
- Spark Execution Logs
- CloudWatch Alarms
- SNS Notifications

This enables rapid troubleshooting and production monitoring.

---

# Complete Production Flow

```text
                Batch Processing

Finnhub REST API

↓

Python ETL

↓

Docker

↓

Amazon ECR

↓

Amazon ECS (Fargate)

↓

Amazon S3 Raw

↓

Amazon EMR + Apache Spark

↓

Data Quality Validation

↓

Apache Iceberg

↓

AWS Glue Catalog

↓

Amazon Athena



                Streaming Processing

Finnhub WebSocket

↓

Python Producer

↓

Amazon Kinesis

↓

Python Consumer

↓

Amazon S3 Streaming

↓

Apache Spark

↓

Bronze

↓

Silver

↓

Gold
```

---

# Skills Demonstrated

## Programming

- Python
- SQL
- PySpark

## AWS

- Amazon ECS
- AWS Fargate
- Amazon ECR
- Amazon S3
- Amazon EMR
- Amazon Kinesis
- AWS Glue
- Amazon Athena
- Amazon Redshift
- Amazon CloudWatch
- IAM

## Data Engineering

- REST API Integration
- Streaming Pipelines
- ETL
- Data Lakes
- Lakehouse Architecture
- Apache Iceberg
- Distributed Processing
- Data Quality Engineering

## DevOps

- Docker
- GitHub Actions
- Terraform
- Git

---

# Project Status

## Completed

- Python ETL Pipeline
- Docker
- Amazon ECS
- Amazon ECR
- Amazon S3
- Amazon EMR
- Apache Spark
- Amazon Kinesis
- Data Quality Validation
- Apache Iceberg
- AWS Glue
- Amazon Athena
- Amazon Redshift
- Airflow
- Terraform
- GitHub Actions
- CloudWatch

---

## Next Enhancements

- Power BI Dashboard
- EventBridge Scheduling
- Secrets Manager
- Incremental Iceberg Writes

---

# Key Takeaways

This project demonstrates how multiple AWS services integrate to form a production-style cloud-native data engineering platform.

Key concepts implemented include:

- Batch Processing
- Real-Time Streaming
- Data Lakes
- Lakehouse Architecture
- Data Warehousing
- Distributed Processing
- Containerization
- Workflow Orchestration
- Infrastructure as Code
- CI/CD
- Monitoring
- Cloud Security