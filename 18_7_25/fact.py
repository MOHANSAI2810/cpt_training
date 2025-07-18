# def sum_digits(a):
#     n = 0
#     while a > 0:
#         n += a % 10   # add last digit to n
#         a = a // 10   # remove last digit
#     return n
# sum=(lambda x:lambda n:0 if n==0 else n%10 +x(x)(n//10))(lambda x:lambda n:0 if n==0 else n%10 +x(x)(n//10))
# print(sum(3246))  # Output: 15 (3 + 2 + 4 + 6)
a=(lambda x:lambda n:0 if n==0 else n%10+x(x)(n//10))(lambda x:lambda n:0 if n==0 else n%10+x(x)(n//10))
print(a(1234))