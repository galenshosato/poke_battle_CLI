import requests
import json
import random

class Version:
    def __init__(self, number):
        self.number = number
        
        

    def get_pokemon(self, index):
        response = requests.get(f'https://pokeapi.co/api/v2/pokedex/{index}')
        version_object = json.loads(response.text)
        poke_entries = version_object['pokemon_entries']
        rand_pokemon = random.randint(0, len(poke_entries)-1)
        pokemon_name = version_object['pokemon_entries'][rand_pokemon]['pokemon_species']['name']
        return pokemon_name

