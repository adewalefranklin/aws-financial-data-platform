from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    dayofmonth,
    from_unixtime,
    lit,
    month,
    to_timestamp,
    trim,
    when,
    year,
)

spark = (
    SparkSession.builder.appName("FinnhubQuotesToIceberg")
    .config(
        "spark.sql.extensions",
        "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
    )
    .config(
        "spark.sql.catalog.glue_catalog",
        "org.apache.iceberg.spark.SparkCatalog",
    )
    .config(
        "spark.sql.catalog.glue_catalog.catalog-impl",
        "org.apache.iceberg.aws.glue.GlueCatalog",
    )
    .config(
        "spark.sql.catalog.glue_catalog.warehouse",
        "s3://aws-data-engineering-platform/iceberg/",
    )
    .config(
        "spark.sql.catalog.glue_catalog.io-impl",
        "org.apache.iceberg.aws.s3.S3FileIO",
    )
    .getOrCreate()
)

#
# Configuration

input_path = "s3://aws-data-engineering-platform/raw/finnhub/quotes/"

rejected_output_path = "s3://aws-data-engineering-platform/rejected/finnhub/quotes/"

iceberg_table = "glue_catalog.financial_platform.quotes"


# Read raw multiline JSON from S3
#

quotes_df = (
    spark.read.option("multiLine", "true")
    .option("recursiveFileLookup", "true")
    .json(input_path)
)
# Temporary debugging output for the current EMR run

quotes_df.printSchema()
quotes_df.show(truncate=False)


# Flatten nested Finnhub JSON

flattened_df = quotes_df.select(
    col("symbol"),
    to_timestamp(
        col("timestamp"),
        "yyyyMMdd'T'HHmmssX",
    ).alias("ingestion_timestamp"),
    col("data.c").alias("current_price"),
    col("data.d").alias("change"),
    col("data.dp").alias("percent_change"),
    col("data.h").alias("high_price"),
    col("data.l").alias("low_price"),
    col("data.o").alias("open_price"),
    col("data.pc").alias("previous_close"),
    from_unixtime(col("data.t")).cast("timestamp").alias("market_timestamp"),
)

# Create partition columns

flattened_df = (
    flattened_df.withColumn(
        "year",
        year(col("ingestion_timestamp")),
    )
    .withColumn(
        "month",
        month(col("ingestion_timestamp")),
    )
    .withColumn(
        "day",
        dayofmonth(col("ingestion_timestamp")),
    )
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
        col("market_timestamp").isNull(),
        lit("Invalid market timestamp"),
    )
    .when(
        col("ingestion_timestamp").isNull(),
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

validated_df = validated_df.dropDuplicates(["symbol", "market_timestamp"])


# Separate valid and rejected records


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


# Fail the job when no usable data exists

if total_count == 0:
    raise ValueError("Data-quality validation failed: no records were found.")

if valid_count == 0:
    raise ValueError(
        "Data-quality validation failed: " "no valid records remain after validation."
    )


# Write rejected records to S3

if rejected_count > 0:
    (
        rejected_quotes_df.write.mode("overwrite")
        .partitionBy("year", "month", "day")
        .parquet(rejected_output_path)
    )


#
# Write valid records to Apache Iceberg
#

(
    valid_quotes_df.writeTo(iceberg_table)
    .using("iceberg")
    .partitionedBy("year", "month", "day")
    .createOrReplace()
)


spark.stop()
