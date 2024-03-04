#!usr/bin/env python3
# coding: utf-8

# A Python script I made for Dead by Daylight custom games
# Author: Revan
# Date: 3/3/24

import random
import dbd_art as art
from os import system


player_list = ['Tyler', 'Tim', 'Peyton']
all_killers = [
    'Trapper','Wraith','Hillbilly','Nurse','Shape','Hag','Doctor','Huntress','Cannibal','Nightmare','Pig','Clown','Spirit',
    'Legion','Plague','Ghost Face','Demogorgon','Oni','Deathslinger','Executioner','Blight','Twins','Trickster','Nemesis',
    'Cenobite','Artist','Onryo','Dredge','Mastermind','Knight','Skull Merchant','Singularity','Xenomorph','Good Guy','Unknown'
]
# randomization pool
killer_list = all_killers.copy()

# main functions
def menu():
    '''The main function of the script.'''
    system('clear')
    print(art.logo)
    print('\nPlease select an option:\n')
    print('\n1. Players\n2. Killers\n3. Quit\n')
    m_option = input('>> ').lower()
    if m_option == '1' or m_option == 'players':
        players()
    elif m_option == '2' or m_option == 'killers':
        killers()
    elif m_option == '3' or m_option == 'quit':
        print('\nGoodbye!\n')
        exit()
    else:
        print('\nInvalid input.\n')
        menu()

def players():
    '''Function to select name generation or to add additional players.'''
    system('clear')
    print('\nPlease select an option:\n')
    print('\n1. Who\'s Killer?\n2. Add Players\n3. Remove Players\n4. Return to Menu\n')
    p_option = input('>> ').lower()
    if p_option == '1' or p_option == 'who\'s killer' or p_option == 'who':
        get_player()
    elif p_option == '2' or p_option == 'add players' or p_option == 'add':
        add_players()
    elif p_option == '3' or p_option == 'remove players' or p_option == 'remove':
        remove_players()
    elif p_option == '4' or p_option == 'return to menu' or p_option == 'return' or p_option == 'menu':
        menu()
    else:
        print('\nInvalid input.\n')
        players()

def killers():
    '''Function to select random killer generation or reset the pool.'''
    system('clear')
    print('\nPlease select an option:\n')
    print('\n1. Who Do I Play?\n2. Reset List\n3. Return to Menu\n')
    k_option = input('>> ').lower()
    if k_option == '1' or k_option == 'who do i play' or k_option == 'who':
        get_killer() # finish sub-function
    elif k_option == '2' or k_option == 'reset list' or k_option == 'reset':
        reset_list() # finish sub-function
    elif k_option == '3' or k_option == 'return to menu' or k_option == 'return' or k_option == 'menu':
        menu()
    else:
        print('\nInvalid input.\n')
        killers()

# sub-functions
def add_players():
    '''Function to input additional players into the player list.'''
    system('clear')
    print('\nInput additional players (one at a time).\n')
    extras = input('>> ').title()
    player_list.append(extras)
    print('\nDone?\n')
    done = input('>> ').lower()
    if done == 'yes' or done == 'y':
        players()
    else:
        add_players()
def remove_players():
    '''Function to remove player names from the player list.'''
    system('clear')
    print('\nType the player names you wish to remove (one at a time).\n')
    p_name = input('>> ').title()
    name_index = player_list.index(p_name)
    player_list.pop(name_index)
    print('\nPlayer removed from list.\n')
    print('\nDone?\n')
    yn3 = input('>> ').lower()
    if yn3 == 'yes' or yn3 == 'y':
        players()
    else:
        remove_players()
def get_player():
    '''Function to generate a random player to be killer.'''
    system('clear')
    chosen_p = random.choice(player_list)
    print(f'\nThe killer is: {chosen_p}\n')
    print('\nGenerate new name?\n')
    yn1 = input('>> ').lower()
    if yn1 == 'yes' or yn1 == 'y':
        get_player()
    else:
        players()

def get_killer():
    '''Function to generate a random killer to play.'''
    system('clear')
    chosen_k = random.choice(all_killers)
    print(f'\nYour killer is: {chosen_k}\n')
    print('\nPlease select an option:\n')
    print('\n1. Regenerate Killer\n2. Remove Killer from Pool\n3. Return\n')
    yn2 = input('>> ').lower()
    if yn2 == '1' or yn2 == 'regenerate killer' or yn2 == 'regenerate' or yn2 == 'regen':
        get_killer()
    elif yn2 == '2' or yn2 == 'remove' or yn2 == 'remove killer' or yn2 == 'remove killer from pool':
        killer_index = killer_list.index(chosen_k)
        killer_list.pop(killer_index)
        print('\nKiller removed from pool.\n')
        input()
        killers()
    elif yn2 == '3' or yn2 == 'return':
        killers()
    else:
        print('\nInvalid input.\nReturning to Killer menu...\n')
        input()
        killers()
def reset_list():
    '''Function to reset the killer pool.'''
    system('clear')
    killer_list = all_killers.copy()
    print('\nList reset!\n')
    input()
    killers()


# initiate program
menu()