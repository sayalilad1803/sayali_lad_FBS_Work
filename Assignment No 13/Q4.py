n = int(input("Enter number: "))

d = {}

for x in range(1, n + 1):
    d[x] = x * x

print("Generated Dictionary:", d)