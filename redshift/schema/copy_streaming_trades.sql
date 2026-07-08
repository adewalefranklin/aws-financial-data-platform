COPY bronze.finnhub_streaming_trades
FROM 's3://aws-data-engineering-platform/processed/finnhub/streaming_trades/'
IAM_ROLE 'arn:aws:iam::972775291781:role/RedshiftDataEngineeringCertRole'
FORMAT AS PARQUET;