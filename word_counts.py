# Ask for input
text = input("Give me some text: \n")

# Clean the text
text = text.lower().replace(',', '').replace('.', '')

# Make a set of unique words, count them and store in dict
unique_words = set(text.split())
counts = {word: text.count(word) for word in unique_words}

# Sort the dict on value
counts = sorted(list(counts.items()), key=lambda x:x[1], reverse=True)

# Print the output
for (word, count) in counts:
    print(f'The word {word} occurs {count} times')