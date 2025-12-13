text = input("Enter a string: ")

freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1

print("Word Frequency:", freq)