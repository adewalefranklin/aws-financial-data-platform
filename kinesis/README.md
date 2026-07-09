# Amazon Kinesis

## Purpose

This module contains the real-time streaming components of the financial data engineering platform.

## Responsibilities

- Connect to Finnhub WebSocket
- Produce real-time financial events into Amazon Kinesis Data Streams
- Consume records from Kinesis
- Land streaming data into Amazon S3 for downstream processing

## Workflow

Finnhub WebSocket
→ Python Producer
→ Amazon Kinesis Data Stream
→ Python Consumer
→ Amazon S3 Raw Streaming Layer

# Kinesis Streaming Pipeline Architecture

Finnhub WebSocket
        ↓
Python Producer
        ↓
Amazon Kinesis Data Streams
        ↓
Python Consumer
        ↓
Amazon S3 Raw Streaming JSON
        ↓
Apache Spark on EMR
        ↓
Amazon S3 Processed Parquet
        ↓
Amazon Redshift
        ↓
Streaming Analytics Tables



This module extends the platform from batch processing into real-time data ingestion.