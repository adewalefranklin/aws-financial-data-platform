from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, year, month, dayofmonth, hour


def main():
    spark = (
        SparkSession.builder
        .appName("Finnhub Streaming Trades To Parquet")
        .getOrCreate()
    )

    input_path = "s3://aws-data-engineering-platform/raw/finnhub/streaming/"
    output_path = "s3://aws-data-engineering-platform/processed/finnhub/streaming_trades/"

    print(f"Reading streaming JSON from: {input_path}")
    print(f"Writing processed Parquet to: {output_path}")

    df = spark.read.json(input_path)

    trades_df = (
        df.select(
            col("symbol"),
            col("price").cast("double").alias("trade_price"),
            col("volume").cast("double").alias("trade_volume"),
            col("event_timestamp").cast("long").alias("event_timestamp")
        )
        .withColumn(
            "trade_timestamp",
            to_timestamp((col("event_timestamp") / 1000).cast("double"))
        )
        .withColumn("year", year("trade_timestamp"))
        .withColumn("month", month("trade_timestamp"))
        .withColumn("day", dayofmonth("trade_timestamp"))
        .withColumn("hour", hour("trade_timestamp"))
    )

    print("Schema:")
    trades_df.printSchema()

    print(f"Record count: {trades_df.count()}")

    (
        trades_df.write
        .mode("append")
        .partitionBy("year", "month", "day", "hour", "symbol")
        .parquet(output_path)
    )

    spark.stop()
    print("Streaming trades Parquet job completed.")


if __name__ == "__main__":
    main()