import boto3
from src.project_pipeline.config import Config
from src.project_pipeline.exceptions import LoadError
from src.project_pipeline.logger import get_logger
from datetime import datetime, timezone
import json
from botocore.exceptions import ClientError, BotoCoreError

class S3Load:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.config = Config()
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=self.config.aws_access_key_id,
            aws_secret_access_key=self.config.aws_secret_access_key,
            region_name=self.config.aws_region
        )
        self.s3_bucket_name = self.config.aws_bucket_name
        self.s3_prefix = self.config.aws_s3_prefix

    def load_to_s3(self, data: dict, symbol: str):
        self.logger.info(f"Loading data to S3 for symbol: {symbol}")
        symbol = symbol.upper().strip()
        now = datetime.now(timezone.utc)

        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        timestamp = now.strftime("%Y%m%dT%H%M%SZ")
        payload = {
            "symbol": symbol,
            "timestamp": timestamp,
            "data": data
        }
        s3_key = (
                    f"{self.s3_prefix}/"
                    f"year={year}/"
                    f"month={month}/"
                    f"day={day}/"
                    f"symbol={symbol}/"
                    f"{timestamp}.json"
                )

        try:
            self.s3_client.put_object(
                Bucket=self.s3_bucket_name,
                Key=s3_key,
                Body=json.dumps(payload, indent=4).encode("utf-8"),
                ContentType="application/json"
            )
            self.logger.info(f"Successfully loaded data to S3 for symbol: {symbol} at {s3_key}")
            return s3_key
        except (ClientError, BotoCoreError) as e:
            self.logger.error(f"Error loading data to S3 for symbol: {symbol} - {e}")
            raise LoadError(f"Error loading data to S3 for symbol: {symbol}") from e


