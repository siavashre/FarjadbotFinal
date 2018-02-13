import json
from handler import user
class AddProvience():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addProvience(self, bot, message, current_state):
        user.provience=message.text
        return self.states[current_state]["nextState"]["register"]

