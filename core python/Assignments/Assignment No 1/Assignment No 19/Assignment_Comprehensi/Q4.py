# Take input from user
string = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Remove vowels
result = ""
for ch in string:
    if ch not in vowels:
        result += ch

print("String after removing vowels:", result)