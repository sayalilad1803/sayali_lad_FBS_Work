l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
r = float(input("Enter radius: "))

area = (l * b) + (0.5 * 3.14 * r * r)
perimeter = (2 * l + b) + (3.14 * r)

print("Area =", area)
print("Perimeter =",perimeter)