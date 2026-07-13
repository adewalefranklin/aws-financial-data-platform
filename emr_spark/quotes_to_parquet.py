from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    dayofmonth,
    lit,
    month,
    to_timestamp,
    trim,
    when,
    year,
)

spark = SparkSession.builder.appName("FinnhubQuotesToParquet").getOrCreate()

# Read raw JSON from S3

input_path = "s3://aws-data-engineering-platform/raw/finnhub/quotes/"

quotes_df = spark.read.json(input_path)

# Flatten JSON

flattened_df = quotes_df.select(
    col("symbol"),
    col("timestamp").alias("ingestion_timestamp"),
    col("data.c").cast("double").alias("current_price"),
    col("data.d").cast("double").alias("change_amount"),
    col("data.dp").cast("double").alias("percent_change"),
    col("data.h").cast("double").alias("high_price"),
    col("data.l").cast("double").alias("low_price"),
    col("data.o").cast("double").alias("open_price"),
    col("data.pc").cast("double").alias("previous_close"),
    col("data.t").cast("long").alias("event_timestamp"),
)

# Convert timestamp

flattened_df = flattened_df.withColumn(
    "quote_timestamp", to_timestamp("ingestion_timestamp", "yyyyMMdd'T'HHmmss'Z'")
)

# Partition columns

flattened_df = (
    flattened_df.withColumn("year", year("quote_timestamp"))
    .withColumn("month", month("quote_timestamp"))
    .withColumn("day", dayofmonth("quote_timestamp"))
)

# Data-quality validation

validated_df = flattened_df.withColumn(
    "validation_error",
    when(
        col("symbol").isNull() | (trim(col("symbol")) == ""),
        lit("Missing symbol"),
    )
    .when(
        col("current_price").isNull(),
        lit("Missing current price"),
    )
    .when(
        col("current_price") <= 0,
        lit("Current price must be greater than zero"),
    )
    .when(
        col("event_timestamp").isNull() | (col("event_timestamp") <= 0),
        lit("Invalid event timestamp"),
    )
    .when(
        col("quote_timestamp").isNull(),
        lit("Invalid ingestion timestamp"),
    )
    .when(
        col("high_price").isNotNull()
        & col("low_price").isNotNull()
        & (col("high_price") < col("low_price")),
        lit("High price cannot be lower than low price"),
    )
    .otherwise(lit(None)),
)

# Remove duplicate stock quotes

validated_df = validated_df.dropDuplicates(["symbol", "event_timestamp"])
valid_quotes_df = validated_df.filter(col("validation_error").isNull()).drop(
    "validation_error"
)

rejected_quotes_df = validated_df.filter(col("validation_error").isNotNull())


# Data-quality metrics

total_count = validated_df.count()
valid_count = valid_quotes_df.count()
rejected_count = rejected_quotes_df.count()

validation_summary = (
    rejected_quotes_df.groupBy("validation_error").count().orderBy(col("count").desc())
)

validation_summary.show(truncate=False)

print(f"Total records: {total_count}")
print(f"Valid records: {valid_count}")
print(f"Rejected records: {rejected_count}")

if total_count == 0:
    raise ValueError("Data-quality validation failed: no records were found.")

if valid_count == 0:
    raise ValueError(
        "Data-quality validation failed: no valid records remain after validation."
    )

# Output locations

valid_output_path = "s3://aws-data-engineering-platform/processed/finnhub/quotes/"

rejected_output_path = "s3://aws-data-engineering-platform/rejected/finnhub/quotes/"

# Write valid records

(
    valid_quotes_df.write.mode("overwrite")
    .partitionBy("year", "month", "day")
    .parquet(valid_output_path)
)

# Write rejected records

(
    rejected_quotes_df.write.mode("overwrite")
    .partitionBy("year", "month", "day")
    .parquet(rejected_output_path)
)
spark.stop()
