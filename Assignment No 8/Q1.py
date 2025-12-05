def rectangle_area(length, breadth):
    area = length * breadth
    return area
l = float(input("Enter the length: "))
b = float(input("Enter the breadth: "))
result = rectangle_area(l, b)
print(result)