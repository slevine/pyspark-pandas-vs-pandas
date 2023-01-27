from datetime import datetime

from pyspark.pandas import read_parquet


start = datetime.now()

df = read_parquet("./data/yellow_tripdata_202*-*.parquet")

print(f"DF has {len(df)} rows.")

res = (
    df.groupby(["PULocationID", "DOLocationID"])
    .agg(
        {
            "total_amount": "sum",
            "fare_amount": "sum",
            "tolls_amount": "sum",
            "tip_amount": "sum",
            "congestion_surcharge": "sum",
            "trip_distance": "mean",
        }
    )
    .sort_values(by="fare_amount", ascending=False)
    .head(10)
)

print(res)
print(f"Runtime: {datetime.now() - start}")
