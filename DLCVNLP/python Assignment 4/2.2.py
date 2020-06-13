def is_vowel(word):
    vowels=['a','e','i','o','u']
    if word in vowels:
        return True
    return False
words=input("Enter words > ")
print(is_vowel(words))