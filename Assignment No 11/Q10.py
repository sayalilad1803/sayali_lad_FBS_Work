nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_list = []

for n in nums:
    if n % 2 != 0:     
        odd_list.append(n)

print("List after removing even numbers:",odd_list)