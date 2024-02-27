import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print('\nWelcome to the password generator!\nPlease input a number for each prompt and you will receive a new password curated to your parameters.\n')

print('\nHow many letters you would like in your password:\n')
n_lets = int(input('>> '))
print('\nHow many numbers you would like in your password:\n')
n_nums = int(input('>> '))
print('\nHow many symbols you would like in your password:\n')
n_syms = int(input('>> '))

print('\nWould you like the order of the characters randomized? Y or N\n')
randomizer = input('>> ').capitalize()


new_pass = ''
for n in range(1, n_lets + 1):
    new_pass += letters[random.randint(0, len(letters) - 1)]
for n in range(1, n_nums + 1):
    new_pass += numbers[random.randint(0, len(numbers) - 1)]
for n in range(1, n_syms + 1):
    new_pass += symbols[random.randint(0, len(symbols) - 1)]
if randomizer == 'Y':
    new_pass = ''.join(random.sample(new_pass, len(new_pass)))


print(f'\nHere is your newly generated password: {new_pass}')