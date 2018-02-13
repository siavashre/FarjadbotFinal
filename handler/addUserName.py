import json
from handler import user
class AddUserName():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addUserName(self, bot, message, current_state):
        user.name=message.text
        return self.states[current_state]["nextState"]["register"]

