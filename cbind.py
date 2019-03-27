def cbind(*data_frames):
    df = pd.concat(data_frames, axis=1, ignore_index=True)
    df.columns = (name for df in data_frames for name in df)
    return df
