def armstrong_sum(n, p):
    if n == 0:
        return 0
    return (n % 10)**p + armstrong_sum(n // 10, p)

num = int(input("Enter number: "))
power = len(str(num))

if armstrong_sum(num, power) == num:
    print("Armstrong number")
else:
    print("Not Armstrong")