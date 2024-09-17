def number_of_vowels(word):
    """
    Counts the number of vowels in a word.

    Args:
    - word (string):  the word to count the vowels of

    Returns:
    - Int: number of vowels
    """
    vowels = "aeiuoy"
    total = 0
    for l in word:
        if l in vowels:
            total += 1

    total = len([l for l in word if l in vowels])

    return total


text = input("Give me a text: \n")
words = text.split()

print(sorted(words, key=number_of_vowels))
        
