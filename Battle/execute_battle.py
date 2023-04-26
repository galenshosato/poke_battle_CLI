import os
import time
from poke_methods import get_pokedex, create_full_pokemon, poke_display, battle


def pokebattle(username):
    game_array = ["Red | Blue | Yellow", 
              'Silver | Gold | Crystal', 
              'Ruby | Sapphire | Emerald', 
              'Diamond | Pearl | Platinum', 
              'Black | Black 2 | White | White 2',
              'X | Y',
              'Sun | Moon',
              'Sword | Shield',
              'Scarlet | Violet']
    os.system('clear')
    print('  Pokemon Battle')
    print('  by Galen Sho Sato')
    time.sleep(2)
    os.system('clear')
    poke_choices = f"""
    Choose Your Game
    
    1) {game_array[0]}
    2) {game_array[1]}
    3) {game_array[2]}
    4) {game_array[3]}
    5) {game_array[4]}
    6) {game_array[5]}
    7) {game_array[6]}
    8) {game_array[7]}
    9) {game_array[8]}
    
    10) Random Choice!
"""
    print(poke_choices)
    game_choice = input("Enter #: ")
    os.system('clear')
    if game_choice == '10':
        print('Risky!')
    else:
        print(f'  {game_array[int(game_choice) - 1]}')
    time.sleep(2)
    print("  Choose your pokemon:")
    en_poke_name = get_pokedex('10')
    en_poke = create_full_pokemon(en_poke_name)
    poke1_name = get_pokedex(game_choice)
    poke1 = create_full_pokemon(poke1_name)
    print(poke_display(poke1))
    choice1 = input("Accept y/n: ")
    if 'y' in choice1:
        battle(poke1, en_poke, username)
    else:
        print("How about this one?")
        poke2_name = get_pokedex(game_choice)
        poke2 = create_full_pokemon(poke2_name)
        print(poke_display(poke2))
        choice2 = input("Accept y/n: ")
        if 'y' in choice2:
            battle(poke2, en_poke, username)
        else:  
            print("Last chance!")
            poke3_name = get_pokedex(game_choice)
            poke3 = create_full_pokemon(poke3_name)
            print(poke_display(poke3))
            choice3 = input("Accept y/n: ")
            if 'y' in choice3:
                battle(poke3, en_poke, username)
            else:
                poke4_name = get_pokedex(game_choice)
                poke4 = create_full_pokemon(poke4_name)
                battle(poke4, en_poke, username)
    time.sleep(2)
    replay = input("Would you like to play again y/n? ")
    if 'y' in replay:
        pokebattle(username)
    else:
       return
    

if __name__ == '__main__':
    pokebattle("Galen")
        