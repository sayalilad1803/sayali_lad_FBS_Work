arr = [34,65,23,56,89,26,46,76,85]

if len(arr) < 2:
    print("List must have at least 2 elements")
else:
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    print("second largest element is:",second)