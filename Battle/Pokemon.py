import requests
import json
import random


class Pokemon:
    def __init__(self, name):
        self.name = name
        self.hp = None
        self.moves = None

    def get_move(self):
        poke_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        poke_object = json.loads(poke_response.text)
        move_num = random.randint(0, (len(poke_object['moves'])-1))
        self.hp = poke_object['stats'][0]['base_stat']
        move = poke_object['moves'][move_num]['move']['url']
        return move

