import pytest
from src.project_pipeline.pipeline import FinnhubPipeline


def test_pipeline_run_success(mocker, monkeypatch):
    # Set environment variables
    monkeypatch.setenv("FINNHUB_API_KEY", "fake_key")
    monkeypatch.setenv("FINNHUB_BASE_URL", "http://fakeurl.com")
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "fake_access_key")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "fake_secret_key")
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    monkeypatch.setenv("AWS_BUCKET_NAME", "fake_bucket")
    monkeypatch.setenv("AWS_S3_PREFIX", "fake_prefix")

    # Mock Extract and S3Load methods
    mocker.patch(
        "src.project_pipeline.extract.Extract.fetch_stock_data",
        return_value={"data": "test_data"},
    )
    mocker.patch(
        "src.project_pipeline.load.S3Load.load_to_s3",
        return_value="s3://fake_bucket/fake_prefix/year=2026/month=07/day=06/symbol=AAPL/data.json",
    )

    pipeline = FinnhubPipeline()
    result = pipeline.run("AAPL")

    assert (
        result
        == "s3://fake_bucket/fake_prefix/year=2026/month=07/day=06/symbol=AAPL/data.json"
    )
