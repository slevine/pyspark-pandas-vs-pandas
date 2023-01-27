import polars as pl
from datetime import datetime

start = datetime.now()

df = pl.read_parquet("./data/2022/yellow_tripdata_2022-*.parquet")

print(f"DF has {len(df)} rows.")

res = (
    df.groupby("DOLocationID", maintain_order=True)
    .agg([pl.col("fare_amount").sum().alias("total_fare")])
    .sort("total_fare", reverse=True)
    .limit(5)
)

print(res)

print(f"Runtime: {datetime.now() - start}")
