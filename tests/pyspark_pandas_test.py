from datetime import datetime

from pyspark.pandas import read_parquet

start = datetime.now()

df = read_parquet("./data/2022/yellow_tripdata_2022-*.parquet")

print(f"DF has {len(df)} rows.")

res = (
    df.groupby("DOLocationID")["fare_amount"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print(res)
print(f"Runtime: {datetime.now() - start}")
