s = input("Enter a string: ")

char_count = 0
for _ in s:
    
    char_count += 1
word_count = len(s.split())

print("Characters:", char_count)
print("Words:",word_count)