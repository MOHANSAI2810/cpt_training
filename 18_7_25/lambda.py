def b(n):
    print('n',n)
    return lambda x:x*n

a=b(2)
print(a(5))