import pandas as pd
print("Enter the 3 names")
names = input().strip().split()
print("Enter the 3 indices")
indices = input().strip().split()
try:
    if len(names) != 3 or len(indices) != 3:
        raise ValueError("Provide the exact names and indices")
    series = pd.Series(data=names, index=indices)
    print(series)
except ValueError as e:
    print(f'Error {e}')