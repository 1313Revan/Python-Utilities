import random

list1 = ['Tyler', 'Tim', 'Peyton', 'Gustavo', 'William']
list2 = []

print('\nPlease select the player list by number that you wish to use.\n')
print('1. Tyler, Tim, Peyton, Gustavo, William\n2. N/A\n')
list_choice = int(input('>> '))

if list_choice == 1:
    names = list1
else:
    pass

chosen = names[random.randint(0, len(names) - 1)]

print(f'\n{chosen} was chosen this time!\n')