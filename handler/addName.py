import json
from util.keyboards import keyboards
from handler import book
class AddName():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addName(self, bot, message, current_state):
        book.name=message.text
        return self.states[current_state]["nextState"]["addBook"]

