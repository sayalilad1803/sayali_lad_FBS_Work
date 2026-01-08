lst = [1, 2, 3, 2, 4, 2, 5]

x = int(input("Enter number to remove: "))

new_list = []

for n in lst:
    if n != x:
        new_list.append(n)

print("List after removing", x,":",new_list)