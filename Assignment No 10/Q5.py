lst = [10, 20, 10, 30, 40, 10]

num = int(input("Enter a number: "))

if num in lst:
    print(num, "is present")
    print("It appears", lst.count(num), "times")
else:
    print(num, "is not present")