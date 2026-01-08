def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
def sum_series(n):
    if n == 1:
        return fact(1)
    else:
        return fact(n) + sum_series(n - 1)

n = int(input("Enter value of n: "))
result = sum_series(n)
print(result)