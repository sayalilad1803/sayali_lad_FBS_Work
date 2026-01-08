lst = [10, 21, 4, 45, 66, 93]

even_list = []
odd_list = []

for num in lst:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even elements:", even_list)
print("Odd elements:",odd_list)