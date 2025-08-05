import pandas as pd
df = pd.read_csv('hospital_data.csv')
df['discount'] = df['bill']*0.9
print(df)
sorted_df = df.sort_values('bill', ascending=True)
print('Sorted file\n', sorted_df)