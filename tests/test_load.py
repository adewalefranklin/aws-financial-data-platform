from datetime import datetime, timezone

from src.project_pipeline.load import S3Load


def test_load_to_s3_success(mocker, mock_env):
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
