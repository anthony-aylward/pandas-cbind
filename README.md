# pandas-cbind
R-like `cbind` for pandas data frames. (see [cbind](https://stat.ethz.ch/R-manual/R-devel/library/base/html/cbind.html))

```python
def cbind(*data_frames):
    df = pd.concat(data_frames, axis=1, ignore_index=True)
    df.columns = (column_name for df in data_frames for column_name in df)
    return df
```
