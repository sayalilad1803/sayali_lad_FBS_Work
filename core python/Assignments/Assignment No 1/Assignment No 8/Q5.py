def sum_of_odd(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0:  
            total += i
    return total
n = int(input("Enter the value of n: "))
result = sum_of_odd(n)
print("sum of all prime numbers between is 1 to",n,"is")
print(result)