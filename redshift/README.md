# Amazon Redshift

## Purpose

This module contains the SQL scripts used to build the analytical data warehouse in Amazon Redshift.

## Responsibilities

- Create database schemas
- Create tables
- Load processed Parquet files from Amazon S3 using COPY
- Perform SQL-based ELT transformations
- Prepare analytical datasets for reporting and querying

## Workflow

S3 Processed Parquet
→ Amazon Redshift COPY
→ SQL Transformations
→ Analytics

This module represents the final analytical layer of the data engineering platform.