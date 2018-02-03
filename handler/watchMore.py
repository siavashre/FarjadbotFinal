import json
from util.keyboards import keyboards
class WatchMore():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def watchMore(self, bot, message, current_state):
        if message.text=="Watch More":
            bot.send_message(chat_id=message.chat_id, text="miad",reply_markup=keyboards["watchMore"])
            return self.states[current_state]["nextState"]["watchMore"]
        elif message.text=="Return":
            bot.send_message(chat_id=message.chat_id, text="You are in main page",reply_markup=keyboards["loggedIn"])
            return self.states[current_state]["nextState"]["loggedIn"]
