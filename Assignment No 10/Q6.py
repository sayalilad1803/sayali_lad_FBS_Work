lst = [1, 2, 2, 3, 4, 4, 5]
new_list = []

for x in lst:
    if x not in new_list:
        new_list.append(x)

print("List without duplicates:",new_list)