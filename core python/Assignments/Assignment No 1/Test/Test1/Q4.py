area = float(input("Enter area of one wall: "))
interior = float(input("Enter interior cost per unit: "))
exterior = float(input("Enter exterior cost per unit: "))

interior_cost = area * interior
exterior_cost = area * exterior
total_cost = interior_cost + exterior_cost

print("Interior Cost =", interior_cost)
print("Exterior Cost =", exterior_cost)
print("Total Painting Cost =",total_cost)