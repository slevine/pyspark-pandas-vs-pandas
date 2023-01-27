# Results

## polars

```
DF has 33003832 rows.
shape: (5, 2)
┌──────────────┬────────────┐
│ DOLocationID ┆ total_fare │
│ ---          ┆ ---        │
│ i64          ┆ f64        │
╞══════════════╪════════════╡
│ 132          ┆ 2.0556e7   │
│ 230          ┆ 1.4428e7   │
│ 236          ┆ 1.4097e7   │
│ 161          ┆ 1.3640e7   │
│ 138          ┆ 1.3621e7   │
└──────────────┴────────────┘
Runtime: 0:00:01.293968
```

## pandas

```
DF has 33003832 rows.
DOLocationID
132    20555684.59
230    14427719.84
236    14097305.30
161    13640026.56
138    13621349.90
Name: fare_amount, dtype: float64
Runtime: 0:00:03.935052
```

## pyspark pandas

``` 
DF has 33003832 rows.
DOLocationID
132    2.055568e+07
230    1.442772e+07
236    1.409731e+07
161    1.364003e+07
138    1.362135e+07
Name: fare_amount, dtype: float64
Runtime: 0:00:04.646422
```
