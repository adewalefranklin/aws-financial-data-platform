# Financial Data Engineering Platform

## Overview

An end-to-end AWS Data Engineering platform that ingests real-time financial market data from the Finnhub API, stores raw data in Amazon S3, transforms it using Apache Spark on Amazon EMR, and loads analytics-ready Parquet data into Amazon Redshift.

The project demonstrates production-style cloud data engineering practices including:

- Data ingestion
- Data lake architecture
- Apache Spark ETL
- Amazon EMR
- Amazon S3
- Amazon Redshift
- IAM Security
- Data partitioning
- Columnar storage (Parquet)

---

## Architecture

                         +----------------------+
                         |    Finnhub API       |
                         +----------+-----------+
                                    |
                                    |
                           Python Extraction
                                    |
                                    |
                    +---------------v---------------+
                    |        Amazon S3              |
                    |                               |
                    |      raw/finnhub/quotes       |
                    +---------------+---------------+
                                    |
                                    |
                            Apache Spark
                              Amazon EMR
                                    |
            ------------------------------------------------
            |                                              |
      Flatten JSON                                Type Conversion
            |                                              |
            --------------------+---------------------------
                                 |
                           Partition Data
                    year/month/day/symbol
                                 |
                                 |
                     Write Parquet Files
                                 |
                                 |
                    +------------v-------------+
                    |        Amazon S3         |
                    |                          |
                    | processed/finnhub/quotes |
                    +------------+-------------+
                                 |
                                 |
                        Amazon Redshift
                                 |
                          COPY (PARQUET)
                                 |
                                 |
                      Bronze Analytics Table
                                 |
                                 |
                        SQL Analytics Layer

---

## Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Data Extraction |
| Finnhub API | Market Data |
| Amazon S3 | Data Lake |
| Apache Spark | Distributed Processing |
| Amazon EMR | Spark Cluster |
| Parquet | Columnar Storage |
| Amazon Redshift | Data Warehouse |
| SQL | Analytics |
| IAM | Security |
| VS Code | Development |
| Git/GitHub | Version Control |

---

## Project Structure

aws-ecosystem-project
│
├── src
│     └── project_pipeline
│
├── spark_jobs
│     ├── quotes_to_parquet.py
│     ├── inspect_quotes_parquet.py
│     ├── test_emr.py
│     └── test_read_json.py
│
├── redshift
│     ├── schema
│     │      create_processed_quotes.sql
│     │
│     ├── copy
│     │      copy_processed_quotes.sql
│     │
│     ├── analytics
│     │
│     └── README.md
│
├── tests
│
├── Dockerfile
│
├── requirements.txt
│
└── README.md

---

## Data Flow

### 1. Extract

Python requests live stock quotes from Finnhub.

Example:

AAPL

MSFT

NVDA

---

### 2. Load

Raw JSON is stored inside S3.

```
raw/
    finnhub/
        quotes/
```

---

### 3. Transform

Apache Spark running on Amazon EMR

- Reads JSON
- Flattens nested structures
- Converts to Parquet
- Partitions dataset

```
processed/
    finnhub/
        quotes/
            year=2026/
                month=7/
                    day=6/
                        symbol=AAPL/
                        symbol=MSFT/
                        symbol=NVDA/
```

---

### 4. Load into Redshift

Amazon Redshift loads Parquet directly from S3 using COPY.

---

## Spark Transformation

Input

Nested JSON

↓

Flatten

↓

Type Casting

↓

Partition

↓

Parquet

---

## Data Model

Columns

symbol

timestamp

current_price

high_price

low_price

open_price

previous_close_price

quote_unix_time

---

## Learning Outcomes

✔ Amazon S3

✔ Apache Spark

✔ Amazon EMR

✔ Apache Parquet

✔ Redshift COPY

✔ IAM Roles

✔ Distributed Processing

✔ Spark Partitioning

✔ Production Debugging

✔ ETL Design

---

## Future Improvements

Real-Time Streaming (Kinesis)

Apache Iceberg

Incremental Loads

Airflow Orchestration

CloudWatch Monitoring

Terraform Infrastructure

CI/CD

Data Quality Validation
