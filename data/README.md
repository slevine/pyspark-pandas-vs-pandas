### Get Data

- Download taxi data asynchronously with this simple one liner

```bash
mkdir 2019
cd 2019
for i in {01..12}; do curl https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-$i.csv -O -s&; done; wait
```

- Note: Only change required is the year from `2019` to `2020`
