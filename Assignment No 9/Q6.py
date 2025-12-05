def fib(n):
    if n <= 1:         
        return n
    return fib(n-1) + fib(n-2)

num = int(input("Enter how many terms: "))

print("Fibonacci series:")
for i in range(num):
    print(fib(i),end=' ')