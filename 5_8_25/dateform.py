import pandas as pd
df = pd.read_csv('hospital_data.csv')
series = df['date']
print(series)
confirm=input("Want to convert to date?").strip().lower()
    date = pd.to_datetime(series, format='%Y-%m-%d')
    f_series=date.dt.strftime('%d-%m-%Y')
    print(date)
else:
    print("thank you")
