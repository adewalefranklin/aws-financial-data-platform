# EMR Spark

## Purpose

This module contains all Apache Spark jobs executed on Amazon EMR.

These jobs transform raw Finnhub JSON data stored in Amazon S3 into
partitioned Parquet datasets for analytical querying in Amazon Redshift.

---

## Current Jobs

quotes_to_parquet.py

- Reads raw JSON
- Flattens nested JSON
- Casts data types
- Converts timestamps
- Creates partition columns
- Writes partitioned Parquet

inspect_quotes_parquet.py

- Validates transformed Parquet output

test_emr.py

- Test script used during EMR debugging

---

## Deployment

Upload Spark scripts to S3

aws s3 cp emr_spark/jobs/quotes_to_parquet.py \
s3://aws-data-engineering-platform/scripts/

---

## Execution

The EMR Step executes:

spark-submit s3://aws-data-engineering-platform/scripts/quotes_to_parquet.py