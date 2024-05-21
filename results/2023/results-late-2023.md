# Results

_The tests were run on a M1 Max Macbook Pro with 32 GB of Ram_

## polars

```
DF has 70560406 rows.
shape: (52_878, 8)
┌──────────────┬──────────────┬──────────────┬─────────────┬───────────────┬────────────┬──────────────────────┬───────────────┐
│ PULocationID ┆ DOLocationID ┆ total_amount ┆ fare_amount ┆ tolls_amount  ┆ tip_amount ┆ congestion_surcharge ┆ trip_distance │
│ ---          ┆ ---          ┆ ---          ┆ ---         ┆ ---           ┆ ---        ┆ ---                  ┆ ---           │
│ i64          ┆ i64          ┆ f64          ┆ f64         ┆ f64           ┆ f64        ┆ f64                  ┆ f64           │
╞══════════════╪══════════════╪══════════════╪═════════════╪═══════════════╪════════════╪══════════════════════╪═══════════════╡
│ 132          ┆ 265          ┆ 8.7909e6     ┆ 7.4224e6    ┆ 374067.16     ┆ 795700.48  ┆ 8743.25              ┆ 21.956994     │
│ 132          ┆ 230          ┆ 7.8948e6     ┆ 5.7700e6    ┆ 677238.74     ┆ 856887.87  ┆ 271995.25            ┆ 18.305493     │
│ 264          ┆ 264          ┆ 6.9791e6     ┆ 5.2377e6    ┆ 132240.98     ┆ 888590.87  ┆ 373987.5             ┆ 3.256247      │
│ 132          ┆ 48           ┆ 5.8091e6     ┆ 4.2757e6    ┆ 496605.179999 ┆ 605372.31  ┆ 201617.5             ┆ 18.533374     │
└──────────────┴──────────────┴──────────────┴─────────────┴───────────────┴────────────┴──────────────────────┴───────────────┘
```

**Runtime: 0:00:05.623064**

## pandas

```
DF has 70560406 rows.
                           total_amount  fare_amount  tolls_amount  tip_amount  congestion_surcharge  trip_distance
PULocationID DOLocationID
132          265             8790934.51   7422390.32     374067.16   795700.48               8743.25      21.956994
             230             7894806.99   5770019.47     677238.74   856887.87             271995.25      18.305493
264          264             6979146.58   5237721.48     132240.98   888590.87             373987.50       3.256247
132          48              5809088.05   4275710.82     496605.18   605372.31             201617.50      18.533374
             132             4293873.70   3524985.16      69755.77   463964.71               9502.50       2.306788
             164             4510414.60   3247564.82     397416.61   535699.93             153245.50      17.439196
138          230             4889752.34   3229509.35     565195.92   658726.95             224610.00      10.480836
237          236             5733423.01   3215118.36        191.12   778307.03            1184262.50       1.093344
236          237             5143731.00   2978173.55        255.04   691773.73            1010782.50       1.156337
132          170             4112882.90   2963877.08     361501.95   493218.45             138960.00      17.076423
```

**Runtime: 0:00:11.398830**

## pyspark pandas

``` 
DF has 70560406 rows.
                           total_amount  fare_amount  tolls_amount  tip_amount  congestion_surcharge  trip_distance
PULocationID DOLocationID
132          265           8.790935e+06   7422390.32     374067.16   795700.48               8743.25      21.956994
             230           7.894807e+06   5770019.47     677238.74   856887.87             271995.25      18.305493
264          264           6.979147e+06   5237721.48     132240.98   888590.87             373987.50       3.256247
132          48            5.809088e+06   4275710.82     496605.18   605372.31             201617.50      18.533374
             132           4.293874e+06   3524985.16      69755.77   463964.71               9502.50       2.306788
             164           4.510415e+06   3247564.82     397416.61   535699.93             153245.50      17.439196
138          230           4.889752e+06   3229509.35     565195.92   658726.95             224610.00      10.480836
237          236           5.733423e+06   3215118.36        191.12   778307.03            1184262.50       1.093344
236          237           5.143731e+06   2978173.55        255.04   691773.73            1010782.50       1.156337
132          170           4.112883e+06   2963877.08     361501.95   493218.45             138960.00      17.076423
```

**Runtime: 0:00:06.473986**

## pyspark dataframe

```
DF has 70560406 rows.
+------------+------------+------------------+------------------+------------------+------------------+-------------------------+------------------+
|PULocationID|DOLocationID| sum(total_amount)|  sum(fare_amount)| sum(tolls_amount)|   sum(tip_amount)|sum(congestion_surcharge)|avg(trip_distance)|
+------------+------------+------------------+------------------+------------------+------------------+-------------------------+------------------+
|         132|         265| 8790934.510000236| 7422390.320000001| 374067.1600000008| 795700.4800000027|                  8743.25|21.956994294661445|
|         132|         230| 7894806.989998972|        5770019.47| 677238.7400001296| 856887.8699999934|                271995.25| 18.30549332223389|
|         264|         264|6979146.5800001435| 5237721.479999993|132240.97999999748| 888590.8700000198|                 373987.5|3.2562468018918778|
|         132|          48| 5809088.049999422|        4275710.82| 496605.1800000536| 605372.3100000018|                 201617.5| 18.53337386798331|
|         132|         132| 4293873.699999663| 3524985.159999996| 69755.77000000024| 463964.7100000004|                   9502.5| 2.306787751783676|
|         132|         164| 4510414.599999686|3247564.8200000003|397416.61000002164| 535699.9300000014|                 153245.5|17.439196178712713|
|         138|         230| 4889752.339999689|3229509.3500000006| 565195.9200000844| 658726.9499999994|                 224610.0|10.480836035837974|
|         237|         236| 5733423.009999143|3215118.3600000055|            191.12| 778307.0300000329|                1184262.5|1.0933443014330708|
|         236|         237|  5143730.99999901|2978173.5500000035|255.04000000000002| 691773.7300000201|                1010782.5| 1.156337053808498|
|         132|         170|4112882.8999997615|2963877.0799999996| 361501.9500000055|493218.45000000193|                 138960.0|17.076423019300243|
+------------+------------+------------------+------------------+------------------+------------------+-------------------------+------------------+
only showing top 10 rows
```

**Runtime: 0:00:04.702448**