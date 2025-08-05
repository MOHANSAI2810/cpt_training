import pandas as pd
df = pd.read_csv('hospital_data.csv')
df['status'] = df['age'].apply(
    lambda x: 'senior citizen' if x > 50 else 'adult' if x > 18 else 'teenage')
print(df)
df.to_csv('hospital_data.csv')
