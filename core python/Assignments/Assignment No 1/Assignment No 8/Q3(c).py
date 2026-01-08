def power_series_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

n = int(input("Enter value of n: "))
result= power_series_sum(n)
print(result)