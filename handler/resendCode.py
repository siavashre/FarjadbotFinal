import json
from util.keyboards import keyboards
class ResendCode():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def resendCode(self, bot, message, current_state):
        if message.text=="Resend Code":
            bot.send_message(chat_id=message.chat_id, text="new code sent to your mobile"+"\n"+"Enter your phone number:")
            return self.states[current_state]["nextState"]["enterCode"]
