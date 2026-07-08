from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Inspect Quotes Parquet").getOrCreate()

path = "s3://aws-data-engineering-platform/processed/finnhub/quotes/"

df = spark.read.parquet(path)

print("Schema:")
df.printSchema()

print(f"Record count: {df.count()}")

df.show(10, truncate=False)

spark.stop()
