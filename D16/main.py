import pandas as pd
import numpy as np

rng = pd.date_range('1/1/2020', periods=10, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)

# print(rng)
# print(ts)
# print(ts.to_period(freq="D"))

def homework():
    index = pd.date_range('1/1/2019', periods=20, freq='D')
    series = pd.Series(range(20), index=index)
    print(series)

    series = series.to_period(freq="W")
    print(series)

    print(series.resample('W').mean())

homework()