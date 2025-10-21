#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    while True:
        s = input("Enter a sentence: ").strip()
        if is_sentence(s):
            return s
        print("Must start with a capital and end with . ! or ?")

def calculate_frequencies(sentence):
    # remove final punctuation, lowercase, split into words
    words = sentence[:-1].lower().split() # Drops last value from the array, makes it lowercase, then splits it into words.
    word_list = []
    freq_list = []
    #loops thorugh all the words than adds 1 for each time it finds it in the array
    for w in words:
        if w in word_list:
            i = word_list.index(w)
            freq_list[i] += 1
        else:
            word_list.append(w)
            freq_list.append(1)
    return word_list, freq_list

# This prints the words and their frequencys  
def print_frequencies(words, freqs):
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(words[i], ":", freqs[i])

# Feeds the values through the functions  
def main():
    s = get_sentence()
    words, freqs = calculate_frequencies(s)
    print_frequencies(words, freqs)

# this makes sure that main is only run when wanted and not when imported 
 if __name__ == "__main__":
    main()
