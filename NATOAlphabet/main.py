# Enter a word to the text prompt, and you'll receive the NATO code words for each letter of the word
# Useful for when you need to spell something out over the phone for example

import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


def input_word():
    user_word = input("\nEnter a word: ").upper()
    code_list = [alphabet_dict[letter] for letter in user_word]

    print(f"\nHere's your NATO code:\n{code_list}")
    go_again()


def go_again():
    answer = input("\nWould you like to enter another word? (y/n)\n").lower()
    if answer == "y" or answer == "yes":
        input_word()
    else:
        print("\nGoodbye!")
        exit()


input_word()
