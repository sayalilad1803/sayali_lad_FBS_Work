sentence = input("Enter a sentence: ")

words = sentence.split()

word_lengths = {word: len(word) for word in words}

print("Length of each word:", word_lengths)