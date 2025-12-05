def armstrong(num):
    temp = num
    digits = len(str(num))
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** digits
        num //= 10
    return total == temp
n = int(input("Enter a number: "))
if armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")