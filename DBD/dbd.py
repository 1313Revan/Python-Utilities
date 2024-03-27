#!/usr/bin/env python3
# coding: utf-8

# A randomization script for Dead by Daylight custom games with friends & family that I made while learning
# Author: Revan

import random

import dbd_art as art

# List of all killers
ALL_KILLERS = [
    'Trapper', 'Wraith', 'Hillbilly', 'Nurse', 'Shape', 'Hag', 'Doctor', 'Huntress', 'Cannibal', 'Nightmare', 'Pig',
    'Clown', 'Spirit', 'Legion', 'Plague', 'Ghost Face', 'Demogorgon', 'Oni', 'Deathslinger', 'Executioner', 'Blight',
    'Twins', 'Trickster', 'Nemesis', 'Cenobite', 'Artist', 'Onryo', 'Dredge', 'Mastermind', 'Knight', 'Skull Merchant',
    'Singularity', 'Xenomorph', 'Good Guy', 'Unknown'
]

# Copy of the initial list of killers
killer_list = ALL_KILLERS.copy()


# Main menu function
def menu():
    """The main function of the script."""
    print(art.logo)
    print('\nPlease select an option:\n')
    print('1. Players\n2. Killers\n3. Quit\n')
    m_option = input('>> ').lower()
    if m_option == '1' or m_option == 'players':
        players_menu()
    elif m_option == '2' or m_option == 'killers':
        killers_menu()
    elif m_option == '3' or m_option == 'quit':
        print('\nGoodbye!\n')
        exit()
    else:
        print('\nInvalid input.\n')
        menu()


# Players menu function
def players_menu():
    """Function to select name generation or to add additional players."""
    print('\nPlease select an option:\n')
    print('1. Who\'s Killer?\n2. Add Players\n3. Remove Players\n4. Return to Menu\n')
    p_option = input('>> ').lower()
    if p_option == '1' or p_option == 'who\'s killer' or p_option == 'who':
        get_random_player()
    elif p_option == '2' or p_option == 'add players' or p_option == 'add':
        add_players()
    elif p_option == '3' or p_option == 'remove players' or p_option == 'remove':
        remove_players()
    elif p_option == '4' or p_option == 'return to menu' or p_option == 'return' or p_option == 'menu':
        menu()
    else:
        print('\nInvalid input.\n')
        players_menu()


# Killers menu function
def killers_menu():
    """Function to select random killer generation or reset the pool."""
    print('\nPlease select an option:\n')
    print('1. Who Do I Play?\n2. Reset List\n3. Return to Menu\n')
    k_option = input('>> ').lower()
    if k_option == '1' or k_option == 'who do i play' or k_option == 'who':
        get_random_killer()
    elif k_option == '2' or k_option == 'reset list' or k_option == 'reset':
        reset_list()
    elif k_option == '3' or k_option == 'return to menu' or k_option == 'return' or k_option == 'menu':
        menu()
    else:
        print('\nInvalid input.\n')
        killers_menu()


# Function to add players
def add_players():
    """Function to input additional players into the player list."""
    print('\nInput additional players (one at a time), type "done" when finished.\n')
    while True:
        player = input('>> ').title()
        if player == 'Done':
            break
        else:
            player_list.append(player)
    players_menu()


# Function to remove players
def remove_players():
    """Function to remove player names from the player list."""
    print('\nType the player names you wish to remove (one at a time).\n')
    while True:
        player = input('>> ').title()
        if player in player_list:
            player_list.remove(player)
            print(f'\n{player} removed from the list.\n')
        else:
            print(f'\n{player} is not in the list.\n')
        done = input('Done? (yes/no): ').lower()
        if done == 'yes' or done == 'y':
            break
    players_menu()


# Function to get a random player
def get_random_player():
    """Function to generate a random player to be the killer."""
    if player_list:
        chosen_player = random.choice(player_list)
        print(f'\nThe killer is: {chosen_player}\n')
        yn1 = input('\nGenerate new name? (yes/no): ').lower()
        if yn1 == 'yes' or yn1 == 'y':
            get_random_player()
        else:
            players_menu()
    else:
        print('\nNo players in the list.\n')
        players_menu()


# Function to get a random killer
def get_random_killer():
    """Function to generate a random killer to play."""
    if killer_list:
        chosen_killer = random.choice(killer_list)
        print(f'\nYour killer is: {chosen_killer}\n')
        yn2 = input('\nRegenerate Killer? (yes/no): ').lower()
        if yn2 == 'yes' or yn2 == 'y':
            get_random_killer()
        elif yn2 == 'no' or yn2 == 'n':
            remove_from_pool = input('\nRemove killer from pool? (yes/no): ').lower()
            if remove_from_pool == 'yes' or remove_from_pool == 'y':
                killer_list.remove(chosen_killer)
                print('\nKiller removed from pool.\n')
            killers_menu()
        else:
            print('\nInvalid input.\n')
            killers_menu()
    else:
        print('\nNo killers in the pool.\n')
        killers_menu()


# Function to reset the killer pool
def reset_list():
    """Function to reset the killer pool."""
    global killer_list
    killer_list = ALL_KILLERS.copy()
    print('\nList reset!\n')
    killers_menu()


# Initiate program
player_list = []
menu()
