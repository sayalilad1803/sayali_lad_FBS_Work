a = float(input("enter value of a:"))
s= 0

for i in range(1, 11):
    s += (a ** i)/i

print("Sum of the series =",s)