import pandas as pd
num=input("ENter 4 numbers").strip().split()
num=[float(x) for x in num]
series=pd.Series(num)
print(series+100)