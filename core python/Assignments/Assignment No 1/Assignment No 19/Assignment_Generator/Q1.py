def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

limit = int(input("Enter the limit"))

for num in fibonacci(limit):
    print(num,end =' ')