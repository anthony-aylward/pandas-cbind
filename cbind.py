def cbind(*data_frames):
    return pd.concat(data_frames, axis=1)
