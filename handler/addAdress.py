import json
from handler import user
class AddAdress():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addAdress(self, bot, message, current_state):
        user.address=message.text
        return self.states[current_state]["nextState"]["register"]

