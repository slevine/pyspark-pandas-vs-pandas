from datetime import datetime

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("ReadTaxi").getOrCreate()

start = datetime.now()

df = spark.read.parquet("./data/yellow_tripdata_202*-*.parquet")

print(f"DF has {df.count()} rows.")

res = (df.groupby(["PULocationID", "DOLocationID"]).agg(
    sum("total_amount"),
    sum("fare_amount"),
    sum("tolls_amount"),
    sum("tip_amount"),
    sum("congestion_surcharge"),
    mean("trip_distance")
).sort(desc(sum("fare_amount"))).show(10))

print(f"Runtime: {datetime.now() - start}")
