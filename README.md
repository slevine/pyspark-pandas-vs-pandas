### Simple Dataframe Comparison

The goal of the code used was to highlight the fact that the only thing that
needs to change in order to leverage Pandas API on Spark vs Pandas is to change
an import. Since the frameworks do not handle reading in multiple files the same
exact way, a few changes were required in order to achieve the same results.

### Requirements

- `python > 3.10`
- [poetry][poetry]

### Setup

- Download 2021 and all available 2022 data   

```bash
mkdir data
cd data
for i in {01..12}; do curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-$i.parquet -O -s&; done; wait
for i in {01..10}; do curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-$i.parquet -O -s&; done; wait
```

```bash
poetry install
```

### Running

- To run the `polars` version

```bash
python tests/polars_test.py
```

- To run the `pyspark pandas` version

```bash
python tests/pyspark_pandas_test.py
```

- To run the `plain pandas` version

```bash
python tests/tests/pandas_test.py
```
   
Alternatively, you can use this [notebook][TestRuns] to run the tests by starting a `jupyter-lab` after running `poetry install`

### Additional Details

- [Accompanying Blog Post][post]

### Change Log

#### Early 2023

- Added a Notebook to showing the test runs
- Upgraded `pyspark` to `3.3.1`
- Upgraded `pandas` to `1.5.3`
- Added 2022 dataset
- Changed file type to Parquet
- Added `polars` test
                                                  
[poetry]: https://python-poetry.org/

[TestRuns]: TestRuns.ipynb

[post]: https://stevenlevine.dev/2022/01/pandas-on-spark-vs-plain-pandas/


