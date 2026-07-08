CREATE TABLE analytics.trade_analysis_table
AS
SELECT
    DATE_TRUNC('minute', trade_timestamp) AS trade_minute,
    COUNT(*) AS trade_count,
    AVG(trade_price) AS avg_price,
    SUM(trade_volume) AS total_volume
FROM bronze.finnhub_streaming_trades
GROUP BY 1
ORDER BY 1;
