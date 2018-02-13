import json
from handler import user
class AddEmail():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addEmail(self, bot, message, current_state):
        user.email=message.text
        return self.states[current_state]["nextState"]["register"]

