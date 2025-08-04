import pandas as pd
import numpy as np
series = pd.Series([1, np.nan, 2, np.nan, 3, np.nan, 4], index=[1, 2, 3, 4, 5, 6, 7])
print(series)
print(series.isna())
print(series.fillna('salesforce ✅'))
