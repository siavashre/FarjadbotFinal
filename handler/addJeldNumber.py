import json
from util.keyboards import keyboards
from handler import book
class AddJeldNumber():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addJeldNumber(self, bot, message, current_state):
        book.jeld_num=message.text
        return self.states[current_state]["nextState"]["addBook"]

