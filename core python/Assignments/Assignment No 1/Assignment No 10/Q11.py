lst = [10, 12, 15, 20, 24, 30]

m = int(input("Enter m: "))
n = int(input("Enter n: "))

result = []

for x in lst:
    if x % m == 0 and x % n == 0:
        result.append(x)

print("Numbers divisible by", m, "and",n,":",result)