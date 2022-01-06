from datetime import datetime

from pyspark.pandas import read_csv

start = datetime.now()

pdf = read_csv("./data/2020/yellow_tripdata_2020-*.csv")

print(pdf.count())

res = pdf.groupby("DOLocationID")["fare_amount"] \
    .sum() \
    .sort_values(ascending=False) \
    .head(10)

print(res)
print(f"Runtime: {datetime.now() - start}")
