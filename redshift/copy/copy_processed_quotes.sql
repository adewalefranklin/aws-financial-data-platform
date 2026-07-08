COPY bronze.finnhub_quotes_processed
FROM 's3://aws-data-engineering-platform/processed/finnhub/quotes/'
IAM_ROLE 'my-redshift-iam-role-arn>'
FORMAT AS PARQUET;