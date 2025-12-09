text = input("Enter a string: ")

count = 0

for char in text:
    if char.islower():
        count += 1
        
print("Number of lowercase letters:",count)