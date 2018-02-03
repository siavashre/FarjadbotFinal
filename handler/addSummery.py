import json
from util.keyboards import keyboards
from handler import book
class AddSummery():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addSummery(self, bot, message, current_state):
        book.summery=message.text
        return self.states[current_state]["nextState"]["addBook"]

