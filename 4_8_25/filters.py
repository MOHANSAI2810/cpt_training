import pandas as pd
print("Enter the 3 indices")
indices = input().strip().split()
indices = [float(num) for num in indices]
try:
    if len(indices) != 3:
        raise ValueError("Provide the exact indices")
    series = pd.Series(indices)
    print(series)
    filtered = series[series > 10]
    print(filtered)
except ValueError as e:
    print(f'Error {e}')
