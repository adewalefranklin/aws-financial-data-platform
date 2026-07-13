from datetime import datetime, timezone

from src.project_pipeline.load import S3Load


def test_load_to_s3_success(mocker, monkeypatch):
    monkeypatch.setenv("FINNHUB_API_KEY", "fake_key")
    monkeypatch.setenv("FINNHUB_BASE_URL", "http://fakeurl.com")
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "fake_access_key")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "fake_secret_key")
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    monkeypatch.setenv("AWS_BUCKET_NAME", "fake_bucket")
    monkeypatch.setenv("AWS_S3_PREFIX", "fake_prefix")

    fixed_time = datetime(2026, 7, 6, 12, 30, 45, tzinfo=timezone.utc)

    mock_datetime = mocker.patch("src.project_pipeline.load.datetime")
    mock_datetime.now.return_value = fixed_time

    s3_load = S3Load()
    mock_s3_client = mocker.patch.object(s3_load, "s3_client")

    data = {"key": "value"}
    symbol = "AAPL"

    result = s3_load.load_to_s3(data, symbol)

    expected_key = (
        "fake_prefix/"
        "year=2026/month=07/day=06/"
        "symbol=AAPL/"
        "20260706T123045Z.json"
    )

    assert result == expected_key

    mock_s3_client.put_object.assert_called_once()