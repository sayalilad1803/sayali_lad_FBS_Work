n = int(input("Enter 3 digit number: "))

a = n // 100
b = (n // 10) % 10
c = n % 10

if a == 2 * b and a * 2 == c:
    print("Yes, you have done it")
else:
    print("Please try next time")