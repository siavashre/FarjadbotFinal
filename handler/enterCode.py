import json
from util.keyboards import keyboards
class EnterCode():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def checkCode(self, bot, message, current_state):
        # print(1)
        if message.text=='12345':
            bot.send_message(chat_id=message.chat_id, text="شما وارد حساب کاربری خورد شدید",reply_markup=keyboards["loggedIn"])
            return self.states[current_state]["nextState"]["loggedIn"]
        else:
            # print(2)
            bot.send_message(chat_id=message.chat_id, text="کد شما نادرست است"+"\n"+"لطفا دکمه ارسال مجدد را فشار دهید",reply_markup=keyboards["resendCode"])
            return self.states[current_state]["nextState"]["resendCode"]
