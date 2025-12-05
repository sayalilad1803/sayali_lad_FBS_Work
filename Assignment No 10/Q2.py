def maX(li):
    max = li[0]
    for ind in range(0, len(li)):
        if(max<li[ind]):
            max = li[ind]
    return max

li = [34,65,23,56,89,26,46,76,85]
max_ele = max(li)
print("Maximum ele is", max_ele)


def min(li):
    min = li[0]
    for ind in range(0, len(li)):
        if(min>li[ind]):
            min = li[ind]
    return min

li = [34,65,23,56,89,26,46,76,85]
min_ele = min(li)
print("Minimum ele is", min_ele)


