import pandas as pd
print("Enter the 3 strings")
strings = input().strip().split()
sub = input("Enter the sub string").strip()
try:
    if len(strings) != 3:
        raise ValueError("Provide the exact indices")
    series = pd.Series(strings)
    print(series)
    filtered_strings = series[series.str.lower(
    ).str.contains(sub.lower(), na=False)]
    print(filtered_strings)
except ValueError as e:
    print(f'Error {e}')
