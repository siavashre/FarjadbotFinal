import json
import requests
class EnterPhoneNumber():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def checkPhoneNumber(self, bot, message, current_state):
        # if msg.contact.user_id != msg.chat_id
        if message.text=='null':
            bot.send_message(chat_id=message.chat_id, text=message.text)
        else:
            bot.send_message(chat_id=message.chat_id, text=message['contact']['phone_number'])
        return self.states[current_state]["nextState"]["enterCode"]
