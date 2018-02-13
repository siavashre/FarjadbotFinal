import json
from handler import user
class AddJob():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addJob(self, bot, message, current_state):
        user.job=message.text
        return self.states[current_state]["nextState"]["register"]

