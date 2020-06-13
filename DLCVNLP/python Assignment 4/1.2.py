def filter_long_words(word,n): 
    filtered_words=[w for w in word if len(w)>n]
    print(filtered_words)
def main():
    words=[w for w in input("Enter words to filter >").split(" ")]
    filter_len= int(input("Enter Filter Length>"))
    filter_long_words(words,filter_len)
if __name__ == "__main__":
    main()