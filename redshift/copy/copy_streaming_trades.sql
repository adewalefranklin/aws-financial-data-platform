COPY bronze.finnhub_streaming_trades
FROM 's3://aws-data-engineering-platform/processed/finnhub/streaming_trades/'
IAM_ROLE 'my-redshift-iam-role-arn'
FORMAT AS PARQUET;