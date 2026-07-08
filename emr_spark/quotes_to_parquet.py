from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    to_timestamp,
    year,
    month,
    dayofmonth
)

spark = (
    SparkSession.builder
    .appName("FinnhubQuotesToParquet")
    .getOrCreate()
)

# Read raw JSON from S3

input_path = "s3://aws-data-engineering-platform/raw/finnhub/quotes/"

quotes_df = spark.read.json(input_path)

# Flatten JSON

flattened_df = (
    quotes_df.select(
        col("symbol"),
        col("timestamp").alias("ingestion_timestamp"),

        col("data.c").cast("double").alias("current_price"),
        col("data.d").cast("double").alias("change_amount"),
        col("data.dp").cast("double").alias("percent_change"),
        col("data.h").cast("double").alias("high_price"),
        col("data.l").cast("double").alias("low_price"),
        col("data.o").cast("double").alias("open_price"),
        col("data.pc").cast("double").alias("previous_close"),
        col("data.t").cast("long").alias("event_timestamp")
    )
)

# Convert timestamp

flattened_df = (
    flattened_df.withColumn(
        "quote_timestamp",
        to_timestamp("ingestion_timestamp", "yyyyMMdd'T'HHmmss'Z'")
    )
)

# Partition columns

flattened_df = (
    flattened_df
    .withColumn("year", year("quote_timestamp"))
    .withColumn("month", month("quote_timestamp"))
    .withColumn("day", dayofmonth("quote_timestamp"))
)

# Write Parquet

output_path = "s3://aws-data-engineering-platform/processed/finnhub/quotes/"

(
    flattened_df.write
    .mode("overwrite")
    .partitionBy("year", "month", "day")
    .parquet(output_path)
)

spark.stop()