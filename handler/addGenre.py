import json
from util.keyboards import keyboards
from handler import book
class AddGenre():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addGenre(self, bot, message, current_state):
        book.genre=message.text
        return self.states[current_state]["nextState"]["addBook"]

