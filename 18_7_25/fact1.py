def sum_digits(a):
    n = 0
    while a > 0:
        n += a % 10   # add last digit to n
        a = a // 10   # remove last digit
    return n

print(sum_digits(3246))  # Output: 15 (3 + 2 + 4 + 6)
