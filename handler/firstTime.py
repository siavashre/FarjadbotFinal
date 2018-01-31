import json
from util.keyboards import keyboards

class FirstTimeHandler():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def start(self, bot, message, current_state):
        bot.send_message(chat_id=message.chat_id, text="Enter your phone number:", reply_markup=keyboards["enterPhoneNumber"])
        return self.states[current_state]["nextState"]["all"]
