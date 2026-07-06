import os
from dotenv import load_dotenv
from src.project_pipeline.exceptions import ConfigError

load_dotenv()


class Config:
    def __init__(self):
        self.finnhub_api_key = os.getenv("FINNHUB_API_KEY")
        self.finnhub_base_url = os.getenv("FINNHUB_BASE_URL")
        if not self.finnhub_api_key:
            raise ConfigError(
                "FINNHUB_API_KEY is not set in the environment variables."
            )
        if not self.finnhub_base_url:
            raise ConfigError(
                "FINNHUB_BASE_URL is not set in the environment variables."
            )
