def sumofele(li):
    sum = 0
    for ind in range(0, len(li)):
        sum = sum + li[ind]
    return sum

li = [10, 20, 30, 40, 50]
result = sumofele(li)
print(result)