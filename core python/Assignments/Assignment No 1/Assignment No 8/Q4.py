def sum_of_odd(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0:   
            total += i
    return total
num = int(input("Enter the value of n: "))
result = sum_of_odd(num)
print("Sum of all odd numbers between 1 to",num,"is:")
print(result)