import json
from handler import user
class AddPN():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addPN(self, bot, message, current_state):
        user.phoneNumber=message.text
        return self.states[current_state]["nextState"]["register"]

