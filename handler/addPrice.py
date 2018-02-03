import json
from util.keyboards import keyboards
from handler import book
class AddPrice():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addPrice(self, bot, message, current_state):
        book.price=int(message.text)
        return self.states[current_state]["nextState"]["addBook"]

