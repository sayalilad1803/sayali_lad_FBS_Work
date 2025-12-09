s = input("Enter a string: ")

new_s = ' '
for i in range(len(s)):
    if i % 2 == 0: 
        new_s += s[i]
print(new_s)