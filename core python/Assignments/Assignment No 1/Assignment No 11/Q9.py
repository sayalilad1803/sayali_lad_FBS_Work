nums = list(range(1, 11))      
squares = []
cubes = []

for n in nums:
    squares.append(n*n)
    cubes.append(n*n*n)

print("Numbers:", nums)
print("Squares:", squares)
print("Cubes:",cubes)