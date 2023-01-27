from datetime import datetime
from glob import glob

from pandas import concat
from pandas import read_parquet

start = datetime.now()

df = concat(
    map(read_parquet, glob("./data/2022/yellow_tripdata_2022-*.parquet")))

print(f"DF has {len(df)} rows.")

res = (
    df.groupby("DOLocationID")["fare_amount"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print(res)
print(f"Runtime: {datetime.now() - start}")
