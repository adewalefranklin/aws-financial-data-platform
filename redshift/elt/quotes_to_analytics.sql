TRUNCATE TABLE staging.stg_finnhub_quotes;

INSERT INTO staging.stg_finnhub_quotes (
    symbol,
    ingestion_timestamp,
    current_price,
    change_amount,
    percent_change,
    high_price,
    low_price,
    open_price,
    previous_close,
    event_timestamp
)
SELECT
    payload.symbol::varchar,
    payload.timestamp::varchar,
    payload.data.c::decimal(18,4),
    payload.data.d::decimal(18,4),
    payload.data.dp::decimal(18,4),
    payload.data.h::decimal(18,4),
    payload.data.l::decimal(18,4),
    payload.data.o::decimal(18,4),
    payload.data.pc::decimal(18,4),
    payload.data.t::bigint
FROM raw_data.finnhub_quote_raw
WHERE payload.symbol IS NOT NULL;


TRUNCATE TABLE analytics.stock_quotes;

INSERT INTO analytics.stock_quotes (
    symbol,
    quote_timestamp,
    current_price,
    change_amount,
    percent_change,
    high_price,
    low_price,
    open_price,
    previous_close
)
SELECT
    symbol,
    TO_TIMESTAMP(ingestion_timestamp, 'YYYYMMDD"T"HH24MISS"Z"'),
    current_price,
    change_amount,
    percent_change,
    high_price,
    low_price,
    open_price,
    previous_close
FROM staging.stg_finnhub_quotes;


