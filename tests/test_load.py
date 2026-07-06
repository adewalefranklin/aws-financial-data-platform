import pytest
from src.project_pipeline.load import S3Load


def test_load_to_s3_success(mocker, monkeypatch):
    # Set environment variables
    monkeypatch.setenv("FINNHUB_API_KEY", "fake_key")
    monkeypatch.setenv("FINNHUB_BASE_URL", "http://fakeurl.com")
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "fake_access_key")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "fake_secret_key")
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    monkeypatch.setenv("AWS_BUCKET_NAME", "fake_bucket")
    monkeypatch.setenv("AWS_S3_PREFIX", "fake_prefix")

    # Create loader
    s3_load = S3Load()

    # Mock S3 client
    mock_s3_client = mocker.patch.object(s3_load, "s3_client")

    # Test data
    data = {"key": "value"}
    symbol = "AAPL"

    # Execute
    result = s3_load.load_to_s3(data, symbol)

    # Assertions
    assert result.startswith(
        f"{s3_load.s3_prefix}/year=2026/month=07/day=06/symbol=AAPL/"
    )

    assert result.endswith(".json")

    mock_s3_client.put_object.assert_called_once()
