import pandas as pd
df = pd.read_csv('hospital_data.csv')
print(df)

group = df.groupby('cause')["bill"].mean()
print(group)
