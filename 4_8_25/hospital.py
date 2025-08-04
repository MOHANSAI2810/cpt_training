import pandas as pd
df=pd.read_csv('hospital_data.csv')
print(df)
print(df.info())
print(df.describe())

print(df.isna())
df_filled=df.copy()
df_filled['name']=df_filled['name'].fillna('Unknown')
df_filled['cause']=df_filled['cause'].fillna('Unknown')
df_filled['age']=df_filled['age'].fillna(df_filled['age'].mean())
print(df_filled)