import pandas as pd
import numpy as np
df = pd.read_csv("hospital_data.csv")
series = df['age']
print(series)
clean_series = series.where((series >= 0) & (series <= 50), np.nan)
print(clean_series)
