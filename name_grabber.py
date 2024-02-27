# Part of Angela Wu's 100 days of code Python bootcamp

import random

print('Type your list of names seperated by a comma and space.\n')
names_string = input('>> ')
names = names_string.split(', ')

chosen = names[random.randint(0, len(names) - 1)]

print(f'{chosen} was chosen this time!')