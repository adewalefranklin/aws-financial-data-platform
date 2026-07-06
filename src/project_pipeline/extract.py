from src.project_pipeline.exceptions import ExtractError
from src.project_pipeline.config import Config
from src.project_pipeline.logger import get_logger
import requests
from requests.exceptions import RequestException


class Extract:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.config = Config()
        self.api_key = self.config.finnhub_api_key
        self.base_url = self.config.finnhub_base_url
        self.quote_endpoint = f"{self.base_url}/quote"

    def fetch_stock_data(self, symbol: str):
        self.logger.info(f"Fetching stock data for symbol: {symbol}")
        symbol = symbol.upper().strip()
        params = {"symbol": symbol, "token": self.api_key}

        try:
            response = requests.get(self.quote_endpoint, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            self.logger.info(f"Successfully fetched stock data for symbol: {symbol}")
            return data
        except RequestException as e:
            self.logger.error(f"Error fetching stock data for symbol: {symbol} - {e}")
            raise ExtractError(f"Error fetching stock data for symbol: {symbol}") from e
