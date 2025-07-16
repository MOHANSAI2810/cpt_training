a=0
b=1
c=2
print(a)
print(b)
print(c)
for i in range(10):
    a=b
    b=c
    c=a+b
    print(c)