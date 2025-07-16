def prime(n):
    if n<=1:
        return 'Prime'
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 'Not Prime'
                break
        else:
            return 'Prime'
a=2
b=7
for i in range(a,b):
    print(f'{i} is {prime(i)}')