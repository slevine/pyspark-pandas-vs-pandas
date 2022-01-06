# Simple util to merge the year's worth of files in to a single one

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.format("csv").load("./data/yellow_tripdata_2020-*.csv")

print(df.count())

df.coalesce(1).write.csv('yellow_tripdata_single.csv')
