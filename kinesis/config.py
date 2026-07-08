import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
KINESIS_STREAM_NAME = os.getenv("KINESIS_STREAM_NAME", "finnhub-trades-stream")
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
FINNHUB_WS_URL = os.getenv("FINNHUB_WS_URL", "wss://ws.finnhub.io")
S3_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME", "aws-data-engineering-platform")
S3_STREAMING_PREFIX = os.getenv("S3_STREAMING_PREFIX", "raw/finnhub/streaming")
