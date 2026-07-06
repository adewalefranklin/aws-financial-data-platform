from src.project_pipeline.pipeline import FinnhubPipeline
from src.project_pipeline.logger import get_logger

logger = get_logger(__name__)


def main():
    pipeline = FinnhubPipeline()

    symbols = ["AAPL", "MSFT", "NVDA"]

    for symbol in symbols:
        try:
            s3_key = pipeline.run(symbol)
            logger.info(f"Data for {symbol} successfully loaded to S3 at {s3_key}")
        except Exception as e:
            logger.error(f"Failed to run pipeline for {symbol}: {e}")
if __name__ == "__main__":
        main()
