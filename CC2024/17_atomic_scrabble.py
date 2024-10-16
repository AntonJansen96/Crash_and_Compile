#!/usr/bin/env python3

import json

dictionary = json.load(open("data/dictionary.json"))

# dictionary = ["hello", "helloworld", "geel", "groen", "gen", "apenstaart", "rietadtten", "trien", 'rapen']


def remove_char_at_index(str, idx):
    return str[:idx] + str[idx + 1 :]


store = []

for word in dictionary:
    # print(f"\n* source word is \"{word}\" *")
    badWord = False

    for test in dictionary:

        # If the test word is longer than the source word, it can never be made
        # from the source word. We also avoid comparing against self.
        if len(test) > len(word) or word == test:
            continue

        testIsASubword = True
        temp = word

        # print(f"Checking the word {test}")

        for letter in test:
            idx = temp.find(letter)
            if idx == -1:
                # print(f"Couldn't find letter \'{letter}\' in \'{temp}\' -> \'{test}\' cannot be made from letters in \'{word}\'.")
                testIsASubword = False
                break
            else:
                # print(f"Found letter \'{letter}\' in \'{temp}\'. Will remove it and continue")
                temp = remove_char_at_index(temp, idx)

        if testIsASubword:
            # print(f"The word \'{test}\' can be made from the letters in \'{word}\'.")
            badWord = True
            break

    if not badWord:
        store.append(word)
        # print(f"\'{word}\' is a good word/possible candidate!")

print(sorted(store, key=len))

# This runs in ~10min on my Macbook Pro M1.
# Could be optimized, and prob much faster in C++.
