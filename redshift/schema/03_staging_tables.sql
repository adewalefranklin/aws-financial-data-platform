CREATE TABLE IF NOT EXISTS staging.stg_finnhub_quotes (
    symbol VARCHAR(20),
    ingestion_timestamp VARCHAR(30),
    current_price DECIMAL(18,4),
    change_amount DECIMAL(18,4),
    percent_change DECIMAL(18,4),
    high_price DECIMAL(18,4),
    low_price DECIMAL(18,4),
    open_price DECIMAL(18,4),
    previous_close DECIMAL(18,4),
    event_timestamp BIGINT,
    loaded_at TIMESTAMP DEFAULT GETDATE()
);