s = input("Enter a string: ")

if len(s) <= 1:
    print(s)
else:
    new_s = s[-1] + s[1:-1] + s[0]
print(new_s)