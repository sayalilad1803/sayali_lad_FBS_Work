def factorial(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f

def sum_factorial_series(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total
n = int(input("Enter a value : "))
result = sum_factorial_series(n)
print(result)