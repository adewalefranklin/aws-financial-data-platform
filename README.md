# Cloud-Native Real-Time Financial Data Platform on AWS


## Overview

An end-to-end cloud-native Data Engineering platform built on AWS that ingests financial market data from the Finnhub REST API and Finnhub WebSocket, processes both batch and streaming workloads, stores raw data in Amazon S3, transforms datasets using Apache Spark on Amazon EMR, loads analytics-ready Parquet datasets into Amazon Redshift, and deploys ingestion pipelines as Docker containers on Amazon ECS using AWS Fargate.

The project demonstrates modern Data Engineering practices including cloud-native data lake architecture, distributed processing, real-time streaming, batch ETL, and analytical data warehousing.

---

## Project Highlights

- End-to-end AWS Data Engineering platform
- Batch and streaming ingestion
- Cloud-native Data Lake architecture
- Dockerized Python ETL pipelines
- Serverless deployment with Amazon ECS and AWS Fargate
- Distributed processing with Apache Spark on Amazon EMR
- Data warehouse implementation using Amazon Redshift
- IAM Role–based authentication (no embedded AWS credentials)
- CloudWatch operational logging

---

## Key Achievements

- Built an end-to-end cloud-native Data Engineering platform on AWS.
- Implemented both batch and real-time streaming ingestion.
- Containerized the ingestion pipeline with Docker.
- Deployed the application on Amazon ECS using AWS Fargate.
- Implemented secure IAM Task Role authentication without embedding AWS credentials.
- Processed raw JSON into analytics-ready Parquet datasets using Apache Spark on Amazon EMR.
- Loaded curated datasets into Amazon Redshift for analytical querying.
- Centralized application logs using Amazon CloudWatch.

---

# Features

## Batch Processing

- REST API ingestion from Finnhub
- Raw JSON landing in Amazon S3
- Apache Spark transformations on Amazon EMR
- JSON to Parquet conversion
- Partitioned Data Lake
- Amazon Redshift loading
- SQL analytics layer

## Streaming Processing

- Finnhub WebSocket integration
- Amazon Kinesis Data Streams
- Python Producer
- Python Consumer
- Real-time JSON landing in Amazon S3
- Apache Spark transformations on Amazon EMR
- Streaming JSON to Parquet conversion
- Amazon Redshift loading
- Streaming analytics layer

# Engineering Practices

- Modular project structure
- IAM Roles and Policies
- Apache Parquet
- Partitioned datasets
- Dockerized development
- Amazon Elastic Container Registry (ECR)
- Amazon Elastic Container Service (ECS)
- AWS Fargate Serverless Containers
- Amazon CloudWatch Logging
- Production-style IAM authentication using Task Roles
- Git version control
- Production-style debugging
- Cloud-native data lake architecture

---

# Architecture

```text
                               BATCH PIPELINE

                     +----------------------------+
                     |      Finnhub REST API      |
                     +-------------+--------------+
                                   |
                                   ▼
                            Python ETL Pipeline
                                   |
                                   ▼
                         Amazon S3 Raw Data Lake
                                   |
                                   ▼
                      Apache Spark on Amazon EMR
                                   |
                  JSON Flattening & Transformations
                                   |
                                   ▼
                    Amazon S3 Processed (Parquet)
                                   |
                                   ▼
                          Amazon Redshift
                                   |
                                   ▼
                       Analytics Data Mart



                            STREAMING PIPELINE

                     +----------------------------+
                     |     Finnhub WebSocket      |
                     +-------------+--------------+
                                   |
                                   ▼
                           Python Producer
                                   |
                                   ▼
                  Amazon Kinesis Data Streams
                                   |
                                   ▼
                           Python Consumer
                                   |
                                   ▼
                   Amazon S3 Raw Streaming Layer
                                   |
                                   ▼
                      Apache Spark on Amazon EMR
                                   |
                         JSON Transformations
                                   |
                                   ▼
                    Amazon S3 Processed (Parquet)
                                   |
                                   ▼
                          Amazon Redshift
                                   |
                                   ▼
                    Streaming Analytics Layer
```

---

---

# Containerized Deployment Architecture

```text
                 Local Development

Python Application
        │
        ▼
Docker Image
        │
        ▼
Amazon Elastic Container Registry (ECR)
        │
        ▼
Amazon ECS Task Definition
        │
        ▼
AWS Fargate
        │
        ├──────────────► Amazon CloudWatch Logs
        │
        ▼
Finnhub REST API
        │
        ▼
Amazon S3 Raw Data Lake
        │
        ▼
Apache Spark on Amazon EMR
        │
        ▼
Amazon S3 Processed (Parquet)
        │
        ▼
Amazon Redshift
        │
        ▼
Power BI
```

The batch ingestion pipeline is packaged as a Docker container, stored in Amazon ECR, executed using Amazon ECS on AWS Fargate, authenticated through IAM Task Roles, and monitored using Amazon CloudWatch Logs.

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Data Engineering |
| Finnhub REST API | Batch Ingestion |
| Finnhub WebSocket | Real-Time Streaming |
| Amazon S3 | Data Lake |
| Apache Spark | Distributed Processing |
| Amazon EMR | Spark Cluster |
| Amazon Kinesis Data Streams | Real-Time Streaming |
| Apache Parquet | Columnar Storage |
| Amazon Redshift | Data Warehouse |
| Amazon ECS | Container Orchestration |
| AWS Fargate | Serverless Container Runtime |
| Amazon ECR | Docker Image Registry |
| Amazon CloudWatch | Application Logging & Monitoring |
| Docker | Containerization |
| IAM Roles | Secure AWS Authentication |
| SQL | Analytics |
| Git & GitHub | Version Control |
| VS Code | IDE |
---

# Project Structure

```text
aws-ecosystem-project
│
├── src
│   └── project_pipeline
│
├── emr_spark
│   ├── quotes_to_parquet.py
│   ├── inspect_quotes_parquet.py
│   ├── streaming_to_parquet.py
│   ├── inspect_streaming_parquet.py
│   └── README.md
│
├── kinesis
│   ├── producer.py
│   ├── consumer.py
│   ├── config.py
│   └── README.md
│
├── redshift
│   ├── analytics
│   ├── copy
│   ├── schema
│   ├── validation
│   └── README.md
│
├── screenshots
│
├── tests
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt
│
└── README.md
```

---

# Batch Data Flow

```text
Finnhub REST API
        │
        ▼
Python ETL
        │
        ▼
Amazon S3 Raw Layer
        │
        ▼
Apache Spark (Amazon EMR)
        │
        ▼
JSON Flattening
        │
        ▼
Data Type Conversion
        │
        ▼
Partitioning
        │
        ▼
Parquet
        │
        ▼
Amazon S3 Processed Layer
        │
        ▼
Amazon Redshift
        │
        ▼
Analytics Data Mart
```

---

# Streaming Data Flow

```text
Finnhub WebSocket
        │
        ▼
Python Producer
        │
        ▼
Amazon Kinesis Data Streams
        │
        ▼
Python Consumer
        │
        ▼
Amazon S3 Raw Streaming Layer
        │
        ▼
Apache Spark (Amazon EMR)
        │
        ▼
JSON Transformation
        │
        ▼
Parquet
        │
        ▼
Amazon S3 Processed Layer
        │
        ▼
Amazon Redshift
        │
        ▼
Streaming Analytics
```

---

# Current Data Lake Layout

```text
Amazon S3

raw/
└── finnhub/
    ├── company_profile/
    ├── news/
    ├── quotes/
    ├── streaming/
    └── symbols/

processed/
└── finnhub/
    ├── quotes/
    └── streaming_trades/

scripts/
```

---



# Data Models

## Batch Quotes

| Column | Description |
|---------|-------------|
| symbol | Stock ticker |
| quote_timestamp | Quote timestamp |
| current_price | Current market price |
| change_amount | Price change |
| percent_change | Percentage change |
| high_price | Daily high |
| low_price | Daily low |
| open_price | Opening price |
| previous_close | Previous closing price |
| event_timestamp | Unix event timestamp |

## Streaming Trades

| Column | Description |
|---------|-------------|
| trade_price | Trade execution price |
| trade_volume | Number of shares traded |
| event_timestamp | Unix timestamp from Finnhub |
| trade_timestamp | Converted timestamp |
| year | Partition year |
| month | Partition month |
| day | Partition day |
| hour | Partition hour |
| symbol | Stock ticker |

---

# AWS Services Used

- Amazon S3
- Amazon EMR
- Amazon Redshift
- Amazon ECS
- AWS Fargate
- Amazon ECR
- Amazon CloudWatch
- Amazon Kinesis Data Streams
- IAM Roles & Policies

---

# AWS Deployment

The batch ingestion pipeline was containerized using Docker and deployed to Amazon ECS using AWS Fargate.

Deployment workflow:

```text
Python Application
        │
Docker Build
        │
Amazon ECR
        │
Amazon ECS Task Definition
        │
AWS Fargate
        │
CloudWatch Logs
        │
Amazon S3
```

The application authenticates to AWS services using IAM Task Roles without embedding AWS access keys inside the container.

---

# Docker

Build image

```bash
docker build -t financial-platform .
```

Run locally

```bash
docker run --rm --env-file .env financial-platform
```

Push to Amazon ECR

```bash
docker push <your-ecr-uri>
```
---

# Container Deployment

- Build Docker image
- Push image to Amazon ECR
- Create ECS Task Definition
- Deploy using AWS Fargate
- Monitor execution in Amazon CloudWatch

---

# Learning Outcomes

- Amazon S3 Data Lake
- REST API ingestion
- WebSocket streaming
- Amazon Kinesis Data Streams
- Python Producer / Consumer architecture
- Apache Spark
- Amazon EMR
- Apache Parquet
- Amazon Redshift
- Amazon ECS
- AWS Fargate
- Amazon ECR
- Amazon CloudWatch
- Docker containerization
- IAM Task Roles
- IAM Execution Roles
- Secure AWS authentication without access keys
- Distributed Processing
- Batch ETL
- Real-Time Data Engineering
- Cloud Data Platform Design
- Production Debugging
- Cloud-native container deployment

---

## Skills Demonstrated

- Cloud Data Engineering
- Distributed Data Processing
- Data Lake Architecture
- Real-Time Streaming
- Batch ETL
- Docker
- AWS Container Services
- IAM Security
- Data Warehousing
- Cloud Monitoring
- Production Deployment

---

# Project Status

## ✅ Completed

- REST API batch ingestion
- WebSocket streaming ingestion
- Amazon Kinesis producer/consumer pipeline
- Amazon S3 Data Lake
- Apache Spark batch processing on Amazon EMR
- Apache Spark streaming processing on Amazon EMR
- JSON to Parquet conversion
- Partitioned datasets
- Amazon Redshift data warehouse
- Batch analytics layer
- Streaming analytics layer
- Docker containerization
- Docker image publishing to Amazon ECR
- Amazon ECS Task Definition
- AWS Fargate deployment
- IAM Task Role authentication
- IAM Execution Role configuration
- Amazon CloudWatch logging
- End-to-end batch execution on AWS
- Production-ready project structure
- GitHub version control

---

# Next Steps

- Apache Airflow orchestration using the Amazon ECS Operator
- Power BI dashboards
- Apache Iceberg
- Terraform Infrastructure as Code
- CI/CD with GitHub Actions
- Data quality validation
- CloudWatch metrics and alarms
- ECS scheduled tasks
- Secrets Manager integration