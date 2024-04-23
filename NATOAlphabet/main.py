# Enter a word to the text prompt, and you'll receive the NATO code words for each letter of the word
# Useful for when you need to spell something out over the phone for example

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_output():
    word = input("\nEnter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please use letters only.")
        generate_output()
    else:
        print(f"\n{output_list}")


generate_output()
