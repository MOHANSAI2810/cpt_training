long=lambda a,b='23456789':a if len(a)>len(b) else b
print(long('123'))