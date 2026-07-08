# Source (Ingestion)

## Purpose

This module contains the Python application responsible for ingesting financial market data from the Finnhub API into Amazon S3.

## Responsibilities

- Connect to the Finnhub REST API
- Extract stock quote data
- Validate API responses
- Upload raw JSON files to Amazon S3 using boto3
- Handle logging and configuration

## Workflow

Finnhub API
→ Python
→ boto3
→ S3 Raw Layer

The raw data stored in S3 is later processed by Apache Spark on Amazon EMR.