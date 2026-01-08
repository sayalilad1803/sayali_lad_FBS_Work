lst = [10, 5, 20, 8, 30]
for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print("Second largest number is:",lst[-2])