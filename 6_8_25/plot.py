import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('hospital_data.csv')
date = df['date']
bill = df['bill']
plt.figure(figsize=(10, 6))
plt.plot(date, bill, color='blue', marker='o')
plt.title('Hospital Bill vs Date')
