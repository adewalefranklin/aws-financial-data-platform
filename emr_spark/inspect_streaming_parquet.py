from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Inspect Streaming Trades Parquet").getOrCreate()

path = "s3://aws-data-engineering-platform/processed/finnhub/streaming_trades/"

print(f"Reading streaming Parquet from: {path}")

df = spark.read.parquet(path)

print("Schema:")
df.printSchema()

print(f"Record count: {df.count()}")

print("Sample records:")
df.show(10, truncate=False)

print("Streaming Parquet inspection completed.")

spark.stop()
