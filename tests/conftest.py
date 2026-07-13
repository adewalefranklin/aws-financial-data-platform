import pytest


@pytest.fixture
def mock_env(monkeypatch):
    monkeypatch.setenv("FINNHUB_API_KEY", "fake_key")
    monkeypatch.setenv("FINNHUB_WS_URL", "wss://fakeurl.com")
    monkeypatch.setenv("FINNHUB_BASE_URL", "http://fakeurl.com")

    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "fake_access_key")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "fake_secret_key")
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    monkeypatch.setenv("AWS_BUCKET_NAME", "fake_bucket")
    monkeypatch.setenv("AWS_S3_PREFIX", "fake_prefix")