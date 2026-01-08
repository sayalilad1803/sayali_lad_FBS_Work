def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        print(a, end=' ')
        a,b=b,a+b
n = int(input("Enter number of terms:"))
print("Fibonacci series:")
fibonacci(n)