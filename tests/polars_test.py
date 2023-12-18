import polars as pl
from datetime import datetime

start = datetime.now()

df = pl.read_parquet("./data/yellow_tripdata_202*-*.parquet")

print(f"DF has {len(df)} rows.")

res = (
    df.group_by(["PULocationID", "DOLocationID"])
    .agg(
        [
            pl.col("total_amount").sum(),
            pl.col("fare_amount").sum(),
            pl.col("tolls_amount").sum(),
            pl.col("tip_amount").sum(),
            pl.col("congestion_surcharge").sum(),
            pl.col("trip_distance").mean(),
        ]
    )
    .sort(by="fare_amount")
    .reverse()
)

print(res)

print(f"Runtime: {datetime.now() - start}")
