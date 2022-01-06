from datetime import datetime
from glob import glob

from pandas import concat
from pandas import read_csv

start = datetime.now()

df = concat(map(read_csv, glob('./data/2020/yellow_tripdata_2020-*.csv')))

print(df.count())

res = df.groupby("DOLocationID")["fare_amount"] \
    .sum() \
    .sort_values(ascending=False) \
    .head(10)

print(res)
print(f"Runtime: {datetime.now() - start}")
