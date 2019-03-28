# pandas-cbind
R-like `cbind` for pandas data frames. (see [cbind](https://stat.ethz.ch/R-manual/R-devel/library/base/html/cbind.html))

```python
def cbind(*data_frames):
    return pd.concat(data_frames, axis=1)
```
