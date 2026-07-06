import os
from dotenv import load_dotenv
from src.project_pipeline.exceptions import ConfigError

load_dotenv()


class Config:
    def __init__(self):
        self.finnhub_api_key = os.getenv("FINNHUB_API_KEY")
        self.finnhub_base_url = os.getenv("FINNHUB_BASE_URL")
        self.aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.aws_region = os.getenv("AWS_REGION")
        self.aws_bucket_name = os.getenv("AWS_BUCKET_NAME")
        self.aws_s3_prefix = os.getenv("AWS_S3_PREFIX")
        if not self.finnhub_api_key:
            raise ConfigError(
                "FINNHUB_API_KEY is not set in the environment variables."
            )
        if not self.finnhub_base_url:
            raise ConfigError(
                "FINNHUB_BASE_URL is not set in the environment variables."
            )
        if not self.aws_access_key_id:
            raise ConfigError(
                "AWS_ACCESS_KEY_ID is not set in the environment variables."
            )
        if not self.aws_secret_access_key:
            raise ConfigError(
                "AWS_SECRET_ACCESS_KEY is not set in the environment variables."
            )
        if not self.aws_region:
            raise ConfigError("AWS_REGION is not set in the environment variables.")
        if not self.aws_bucket_name:
            raise ConfigError(
                "AWS_BUCKET_NAME is not set in the environment variables."
            )
        if not self.aws_s3_prefix:
            raise ConfigError("AWS_S3_PREFIX is not set in the environment variables.")
