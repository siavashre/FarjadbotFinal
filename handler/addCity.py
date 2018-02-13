import json
from handler import user
class AddCity():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addCity(self, bot, message, current_state):
        user.city=message.text
        return self.states[current_state]["nextState"]["register"]

