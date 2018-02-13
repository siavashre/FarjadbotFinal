import json
from handler import user
class AddPassword():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addPassword(self, bot, message, current_state):
        user.passwrod=message.text
        return self.states[current_state]["nextState"]["register"]

