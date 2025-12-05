n = int(input("How many numbers"))

lst = []
for i in range(n):
    lst.append(int(input("Enter number: ")))

even_list = []
odd_list = []

for num in lst:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even list:", even_list)
print("Odd list:",odd_list)