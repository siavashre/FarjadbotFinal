import json
from util.keyboards import keyboards
from handler import book
class AddPageNumber():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addPageNumber(self, bot, message, current_state):
        book.page_num=int(message.text)
        return self.states[current_state]["nextState"]["addBook"]

