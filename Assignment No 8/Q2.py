def circle_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area
r = float(input("Enter the radius of the circle: "))
result = circle_area(r)
print(result)