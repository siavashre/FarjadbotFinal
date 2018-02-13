import json
from handler import user
class AddFamill():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addFamill(self, bot, message, current_state):
        user.famil=message.text
        return self.states[current_state]["nextState"]["register"]

