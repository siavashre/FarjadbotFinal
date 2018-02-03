import json
from util.keyboards import keyboards
class AddBook():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addBook(self, bot, message, current_state):
        print("you are in add boook")