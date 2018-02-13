import json
from handler import user
class AddUser():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addUser(self, bot, message, current_state):
        user.username=message.text
        return self.states[current_state]["nextState"]["register"]

