import json
from util.keyboards import keyboards
class EnterCode():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def checkCode(self, bot, message, current_state):
        # print(1)
        if message.text=='12345':
            bot.send_message(chat_id=message.chat_id, text="Your login to your account",reply_markup=keyboards["addBook"])
        else:
            # print(2)
            bot.send_message(chat_id=message.chat_id, text="Your code is incorrect"+"\n"+"Please touch resend button to send newe code",reply_markup=keyboards["resendCode"])
            return self.states[current_state]["nextState"]["resendCode"]
