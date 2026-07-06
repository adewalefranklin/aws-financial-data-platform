CREATE TABLE IF NOT EXISTS analytics.stock_quotes (
    symbol VARCHAR(20),
    quote_timestamp TIMESTAMP,
    current_price DECIMAL(18,4),
    change_amount DECIMAL(18,4),
    percent_change DECIMAL(18,4),
    high_price DECIMAL(18,4),
    low_price DECIMAL(18,4),
    open_price DECIMAL(18,4),
    previous_close DECIMAL(18,4),
    loaded_at TIMESTAMP DEFAULT GETDATE()
);