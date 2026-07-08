# Real-Time Financial Data Platform on AWS


## Overview

An end-to-end cloud-native Data Engineering platform built on AWS that ingests financial market data from both the Finnhub REST API and Finnhub WebSocket, processes batch and real-time streaming workloads, stores raw data in Amazon S3, transforms datasets using Apache Spark on Amazon EMR, and loads analytics-ready Parquet datasets into Amazon Redshift.

The project demonstrates modern Data Engineering practices including cloud-native data lake architecture, distributed processing, real-time streaming, batch ETL, and analytical data warehousing.

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

## Engineering Practices

- Modular project structure
- IAM Roles and Policies
- Apache Parquet
- Partitioned datasets
- Dockerized development
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
- Analytics Data Mart
- IAM Security
- Distributed Processing
- Batch ETL
- Real-Time Data Engineering
- Cloud Data Platform Design
- Production Debugging

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
- Dockerized development environment
- Modular project documentation
- GitHub version control

---

# Next Steps

- Power BI dashboards
- Apache Airflow orchestration
- Apache Iceberg
- Terraform
- CloudWatch monitoring
- CI/CD pipeline
- Data quality validation