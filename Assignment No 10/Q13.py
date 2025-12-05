lst = [10, 15, 22, 33, 40, 55]

new_list = []

for n in lst:
    if n % 2 != 0:     
        new_list.append(n)

print("List after removing even numbers:",new_list)