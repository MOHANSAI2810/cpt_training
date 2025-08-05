import pandas as pd
df = pd.read_csv('hospital_data.csv')
print(df)
a = int(input("Enter the id of the patient to change"))
b = int(input("Enter the amount to add to the original amount"))
df.loc[df['id'] == a, 'bill'] += b
print(df)
df.to_csv('hospital_data.csv')
