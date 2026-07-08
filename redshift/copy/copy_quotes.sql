COPY raw_data.finnhub_quote_raw
FROM 's3://aws-data-engineering-platform/raw/finnhub/quotes/year=2026/month=07/day=06/'
IAM_ROLE 'my-redshift-iam-role-arn>'
REGION 'us-east-1'
FORMAT AS JSON 'noshred';