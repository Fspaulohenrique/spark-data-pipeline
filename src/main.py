from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

# Create Spark session
spark = SparkSession.builder \
    .appName("Simple Data Pipeline") \
    .getOrCreate()

# Load data
df = spark.read.csv("data/sample_data.csv", header=True, inferSchema=True)

# Show initial data
print("=== Raw Data ===")
df.show()

# Transformations
df_transformed = df.withColumn("value", col("value").cast("int"))

# Aggregation
df_agg = df_transformed.groupBy("action").agg(
    sum("value").alias("total_value")
)

print("=== Aggregated Data ===")
df_agg.show()

# Save output
df_agg.write.mode("overwrite").csv("output/aggregated_data", header=True)

print("Pipeline executed successfully!")
