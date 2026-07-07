COPY bronze.finnhub_quotes_processed
FROM 's3://aws-data-engineering-platform/processed/finnhub/quotes/'
IAM_ROLE 'arn:aws:iam::****:role/RedshiftDataEngineeringCertRole'
FORMAT AS PARQUET;