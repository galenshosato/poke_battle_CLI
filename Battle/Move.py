import requests
import json

class Move:
    def __init__(self, url):
        self.url = url
        self.power = None
        self.name = None
    
    def get_move_details(self):
        move_response = requests.get(f'{self.url}')
        move_object = json.loads(move_response.text)
        move_name = move_object['name']
        move_power = move_object['power']
        self.name = move_name
        self.power = move_power



