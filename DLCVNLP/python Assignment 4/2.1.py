def word_length(word):
    length_words=[len(w) for w in word]
    return length_words
words=[w for w in input("Enter words > ").split(" ")]
print(word_length(words))