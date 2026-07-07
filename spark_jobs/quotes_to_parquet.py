from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def main():
    spark = (
        SparkSession.builder
        .appName("Finnhub Quotes To Parquet")
        .getOrCreate()
    )

    input_path = "s3://aws-data-engineering-platform/raw/finnhub/quotes/"
    output_path = "s3://aws-data-engineering-platform/processed/finnhub/quotes/"

    df = (
        spark.read
        .option("multiline", "true")
        .json(input_path)
    )

    quotes_df = df.select(
        col("symbol"),
        col("timestamp"),
        col("year"),
        col("month"),
        col("day"),
        col("data.c").alias("current_price"),
        col("data.h").alias("high_price"),
        col("data.l").alias("low_price"),
        col("data.o").alias("open_price"),
        col("data.pc").alias("previous_close_price"),
        col("data.t").alias("quote_unix_time")
    )

    quotes_df.printSchema()
    print(f"Record count: {quotes_df.count()}")

    (
        quotes_df.write
        .mode("append")
        .partitionBy("year", "month", "day", "symbol")
        .parquet(output_path)
    )

    spark.stop()


if __name__ == "__main__":
    main()