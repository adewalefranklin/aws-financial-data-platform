# Real-Time Financial Data Platform on AWS

## Overview

An end-to-end cloud-native Data Engineering platform built on AWS that ingests financial market data from the Finnhub REST API and Finnhub WebSocket, processes both batch and streaming workloads, stores data in Amazon S3, transforms datasets using Apache Spark on Amazon EMR, and loads analytics-ready data into Amazon Redshift.

The project demonstrates modern Data Engineering practices including distributed data processing, real-time streaming, data lake architecture, and cloud-native analytics.

---

# Features

## Batch Processing

- REST API ingestion
- Raw JSON landing in Amazon S3
- Apache Spark transformations on Amazon EMR
- JSON to Parquet conversion
- Partitioned Data Lake
- Amazon Redshift loading

## Streaming Processing

- Finnhub WebSocket integration
- Amazon Kinesis Data Streams
- Python Producer
- Python Consumer
- Real-time S3 landing
- Streaming-ready architecture

## Engineering Practices

- Modular project structure
- IAM Roles and Policies
- Apache Parquet
- Partitioned datasets
- Dockerized development
- Git version control
- Production-style debugging

---

# Architecture

```text
                               +----------------------+
                               |    Finnhub REST API  |
                               +----------+-----------+
                                          |
                                          |
                                   Python ETL
                                          |
                                          |
                               Amazon S3 Raw Layer
                                          |
                                          |
                                Apache Spark (EMR)
                                          |
                                  JSON → Parquet
                                          |
                                          |
                           Amazon S3 Processed Layer
                                          |
                                          |
                                Amazon Redshift
                                          |
                                          |
                                   SQL Analytics



                               +----------------------+
                               | Finnhub WebSocket    |
                               +----------+-----------+
                                          |
                                          |
                                  Python Producer
                                          |
                                          |
                             Amazon Kinesis Data Stream
                                          |
                                          |
                                  Python Consumer
                                          |
                                          |
                           Amazon S3 Streaming Layer
```

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
| Amazon Kinesis | Streaming Platform |
| Apache Parquet | Columnar Storage |
| Amazon Redshift | Data Warehouse |
| SQL | Analytics |
| IAM | Security |
| Docker | Development |
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
│   └── README.md
│
├── kinesis
│   ├── producer.py
│   ├── consumer.py
│   ├── config.py
│   └── README.md
│
├── redshift
│   ├── schema
│   ├── copy
│   ├── analytics
│   └── validation
│   └── README.md
│
├── screenshots
│
├── tests
│
├── Dockerfile
│
├── requirements.txt
│
└── README.md
```

---

# Batch Data Flow

```text
Finnhub REST API
        │
        ▼
Python
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
Analytics
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
Amazon Kinesis Data Stream
        │
        ▼
Python Consumer
        │
        ▼
Amazon S3 Streaming Layer
```

---

# Current Data Lake Layout

```text
S3

raw/
└── finnhub/
    ├── quotes/
    └── streaming/

processed/
└── finnhub/
    └── quotes/

scripts/
```

---

# Processed Data Model

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

---

# Learning Outcomes

- Amazon S3 Data Lake
- REST API ingestion
- WebSocket streaming
- Apache Spark
- Amazon EMR
- Amazon Kinesis
- Amazon Redshift
- Apache Parquet
- IAM Security
- Distributed Processing
- Batch ETL
- Streaming Data Engineering
- Production Debugging
- Cloud Data Platform Design

---

# Future Enhancements

- Process streaming data with Apache Spark
- Load streaming data into Amazon Redshift
- Analytics data mart
- Power BI dashboards
- Apache Airflow orchestration
- Apache Iceberg
- Terraform
- CloudWatch monitoring
- CI/CD pipeline
- Data quality validation