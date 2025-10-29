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
        sentence = input("Enter a sentence: ").strip()
        if is_sentence(sentence):
            return sentence
        else:
            print("Invalid sentence. It must start with a capital letter and end with '.', '?', or '!'.")

def calculate_frequencies(sentence):
    # Remove the ending punctuation
    sentence = sentence[:-1]
    # Split sentence into words
    words = sentence.split()

    # Create empty lists
    word_list = []
    freq_list = []

    # Count frequencies
    for word in words:
        word = word.lower()  # Normalize to lowercase
        if word in word_list:
            index = word_list.index(word)
            freq_list[index] += 1
        else:
            word_list.append(word)
            freq_list.append(1)

    return word_list, freq_list

def print_frequencies(words, frequencies):
    print("Word Frequencies:\n")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")

def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)

if __name__ == "__main__":
    main()
