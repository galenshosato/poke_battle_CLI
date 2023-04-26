import random
import os
import time
from Version import Version
from Pokemon import Pokemon
from Move import Move


# This function gets you a pokedex of the chosen game
def get_pokedex(number):
    if number == '1':
        gen1 = Version(1)
        pokemon = gen1.get_pokemon(2)
        return pokemon
    elif number == '2':
        gen2 = Version(2)
        pokemon = gen2.get_pokemon(3)
        return pokemon
    elif number == '3':
        gen3 = Version(3)
        pokemon = gen3.get_pokemon(4)
        return pokemon
    elif number == '4':
        gen4 = Version(4)
        pokemon = gen4.get_pokemon(6)
        return pokemon
    elif number == '5':
        gen5 = Version(5)
        pokemon = gen5.get_pokemon(9)
        return pokemon
    elif number == '6':
        gen6 = Version(6)
        index = random.randint(12, 14)
        pokemon = gen6.get_pokemon(index)
        return pokemon
    elif number == '7':
        gen7 = Version(7)
        index = random.randint(16, 20)
        pokemon = gen7.get_pokemon(index)
        return pokemon
    elif number == '8':
        gen8 = Version(8)
        pokemon = gen8.get_pokemon(27)
        return pokemon
    elif number == '9':
        gen9 = Version(9)
        pokemon = gen9.get_pokemon(31)
        return pokemon
    elif number == '10':
        pokemon = get_random_pokemon()
        return pokemon
    else:
        print("Random Answer gives you Random Pokemon!")
        pokemon = get_random_pokemon()
        return pokemon

# Grabs a random pokemon from the API
def get_random_pokemon():
    rand = Version(10)
    array = [2, 3, 4, 6, 9, 12, 13, 14, 16, 17, 18, 19, 20, 27, 31]
    random_index = random.randint(0, len(array) - 1)
    pokemon = rand.get_pokemon(array[random_index])
    return pokemon


# Creates the pokemon object, including all moves
def create_full_pokemon(name):
    poke = Pokemon(name)
    move_list = create_move_list(poke)
    move_list.sort(key=lambda x: x.power)
    poke.moves = move_list
    return poke


# Creates the movelist for a given pokemon class
def create_move_list(poke):
    move_list = []
    for i in range(3):
        move = create_attack_move(poke)
        if move not in move_list:
            move_list.append(move)
        else:
            move = create_attack_move(poke)
            if move not in move_list:
                move_list.append(move)
            else:
                move = create_attack_move(poke)
                move_list.append(move)
    return move_list

# Ensures that the moves in the list will all be attack moves
def create_attack_move(poke):
    move_url = poke.get_move()
    move = Move(move_url)
    move.get_move_details()
    while move.power == None:
        move_url = poke.get_move()
        move = Move(move_url)
        move.get_move_details()
    return move


# Assigns how much HP is removed based on API power stat
def attack_power(move):
    if move.power <= 50:
        return 10
    elif 50 < move.power <= 100:
        return 20
    else:
        return 40
    
# Generates a random integer that is used to determine whether an attack hits or not
def attack_hit_perc():
    hit_number = random.randint(1, 10)
    return hit_number


# Returns a value that will be subtracted from the HP. This function also determines whether the attack hit or not
def attack_strike(move):
    points = attack_power(move)
    hit_chance = attack_hit_perc()

    if points == 10 and hit_chance < 10:
        return 10
    elif points == 20 and hit_chance <= 6:
        return 20
    elif points == 40 and hit_chance <= 3:
        return 40
    else:
        return 0 
    
# Takes care of the HP that is lost
def battle_logic(def_pokemon, move, hp_loss):
    print(f"{move.name} hit! ")
    def_pokemon.hp = int(def_pokemon.hp) - int(hp_loss)
    
# The basic display of the pokemon
def poke_display(pokemon):
    return f"""

             {pokemon.name}

             HP: {pokemon.hp}

             1) {pokemon.moves[0].name} 2) {pokemon.moves[1].name} 3) {pokemon.moves[2].name}
            
            
            """

# Determines what happens when you win the game
def win_game(en_pokemon, username):
    print(f"{en_pokemon.name} fainted!")
    time.sleep(2)
    print("You win!!!")


# The full battle logic. Everything that happens during the battle happens inside of this method
def battle(pokemon, en_pokemon, username):
    os.system('clear')
    print("Congratulations! You've chosen: ")
    print(poke_display(pokemon))
    time.sleep(5)
    print(f"""
    

              A wild {en_pokemon.name} has appeared!

    
    """)
    time.sleep(3)
    os.system('clear')
    print(poke_display(en_pokemon))
    print(poke_display(pokemon))
    while pokemon.hp > 0:
        print("Choose your attack!")
        move_select = input("Input #: ")
        if '1' in move_select:
            move = pokemon.moves[0]
            move_power = attack_strike(move)
            if move_power != 0:
                time.sleep(2)
                battle_logic(en_pokemon, move, move_power)
                time.sleep(2)
            else:
                time.sleep(2)
                print(f'{move.name} missed!')
                time.sleep(2)
        if '2' in move_select:
            move = pokemon.moves[1]
            move_power = attack_strike(move)
            if move_power != 0:
                time.sleep(2)
                battle_logic(en_pokemon, move, move_power)
                time.sleep(2)
            else:
                time.sleep(2)
                print(f"{move.name} missed!")
                time.sleep(2)
        if '3' in move_select:
            move = pokemon.moves[2]
            move_power = attack_strike(move)
            if move_power != 0:
                time.sleep(2)
                battle_logic(en_pokemon, move, move_power)
                time.sleep(2)
            else:
                time.sleep(2)
                print(f'{move.name} missed!')
                time.sleep(2)
        if en_pokemon.hp <= 0:
            win_game(en_pokemon, username)
            break
        en_pokemon_attack_int = random.randint(0,2)
        en_pokemon_attack = en_pokemon.moves[en_pokemon_attack_int] 
        print(f"{en_pokemon.name} is deciding on an attack...")
        time.sleep(2)
        print(f"{en_pokemon.name} attacks with {en_pokemon_attack.name}")
        en_pokemon_attack_power = attack_strike(en_pokemon_attack)
        if en_pokemon_attack_power != 0:
            time.sleep(2)
            battle_logic(pokemon, en_pokemon_attack, en_pokemon_attack_power)
            time.sleep(2)
            print(poke_display(en_pokemon))
            print(poke_display(pokemon))
        else:
            time.sleep(2)
            print(f'{en_pokemon_attack.name} missed!')
            time.sleep(2)
            print(poke_display(en_pokemon))
            print(poke_display(pokemon))
        if pokemon.hp <= 0:
            print(f"Your {pokemon.name} fainted...")
             
    


