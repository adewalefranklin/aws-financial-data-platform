from src.project_pipeline.extract import Extract
import pytest

def test_extract_success(mocker, monkeypatch):
    monkeypatch.setenv("FINNHUB_API_KEY", "fake_key")
    monkeypatch.setenv("FINNHUB_BASE_URL", "http://fakeurl.com")

    fake_response = mocker.Mock()
    fake_response.raise_for_status.return_value = None
    fake_response.json.return_value = {"data": "test_data"}

    mock_get = mocker.patch(
        "src.project_pipeline.extract.requests.get",
        return_value=fake_response
    )

    extractor = Extract()
    result = extractor.fetch_stock_data("AAPL")

    assert result == {"data": "test_data"}

    mock_get.assert_called_once_with(
        "http://fakeurl.com/quote",
        params={
            "symbol": "AAPL",
            "token": "fake_key"
        },
        timeout=30
    )