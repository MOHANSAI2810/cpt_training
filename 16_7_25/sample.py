# a = [int(x) for x in input().split()][0:9]
# matrix = [[int(not(a[i*3+j]%2==0)) for j in range(3)]for i in range(3)]
# for i in matrix:
#     print(i)
# n=input().split()
# num=[[int(x) for x in n]]
# m=[[num[i*3+j] for j in range(3)] for i in range(3)]
# bm=[[0 if m[i][j]%2==0 else 1 for j in range(3)] for i in range(3)]
# print(m,bm)

for i in range(7):
    for j in range(7):
        if abs(i-3)+abs(j-3) <= 2:
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()
