import json
from handler import user
class AddInviteCode():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addInviteCode(self, bot, message, current_state):
        user.inviteCode=message.text
        return self.states[current_state]["nextState"]["register"]

