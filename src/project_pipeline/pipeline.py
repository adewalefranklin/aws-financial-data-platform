from src.project_pipeline.config import Config
from src.project_pipeline.extract import Extract
from src.project_pipeline.load import S3Load
from src.project_pipeline.logger import get_logger
from src.project_pipeline.exceptions import LoadError

logger = get_logger(__name__)


class FinnhubPipeline:
    def __init__(self):
        self.config = Config()
        self.extractor = Extract()
        self.loader = S3Load()

    def run(self, symbol: str):
        logger.info(f"Starting pipeline for symbol: {symbol}")

        try:
            data = self.extractor.fetch_stock_data(symbol)
            s3_key = self.loader.load_to_s3(data, symbol)

            logger.info(
                f"Pipeline completed successfully for symbol: {symbol}. "
                f"Data loaded to S3 at {s3_key}"
            )

            return s3_key

        except Exception as e:
            logger.error(f"Pipeline failed for symbol: {symbol} - {e}")
            raise LoadError(f"Pipeline failed for symbol: {symbol}") from e
