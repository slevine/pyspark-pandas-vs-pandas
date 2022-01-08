### Simple Dataframe Comparison

The goal of the code used was to highlight the fact that the only thing that needs to change in order to leverage Pandas API on Spark vs Pandas is to change an import. Since the frameworks do not handle reading in multiple files the same exact way, a few changes were required in order to achieve the same results.

### Requirements

- `python`
- [pipenv][pipenv]

### Setup

- [Download Data][data]
- Get code and environment set up

```bash
pipenv install
```

### Running

- To run the `pyspark pandas` version

```bash
python tests/pyspark_pandas_test.py
```

- To run the `plain pandas` version

```bash
python tests/tests/pandas_test.py
```

### Additional Details

- [Accompanying Blog Post][post]

[data]: data/README.md
[pipenv]: https://pipenv.pypa.io/en/latest/
[post]: https://stevenlevine.dev/2022/01/pandas-on-spark-vs-plain-pandas/
