import pandas as pd

num = input("Enter 5 numbers: ").strip().split()
num = [float(x) for x in num]

a = pd.Series(num, index=['a', 'b', 'c', 'd', 'e'])

print("\nOriginal Series:\n", a)

print("\nStatistical Measures:")
print(f"Mean: {a.mean()}")
print(f"Max: {a.max()}")
print(f"Min: {a.min()}")
print(f"Median: {a.median()}")
print(f"Mode:\n{a.mode().to_list()}")

print('index', a.index.to_list())
