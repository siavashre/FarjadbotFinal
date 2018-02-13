import json
from util.keyboards import keyboards
class ResendRegisterCode():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def resnedRegisterCode(self, bot, message, current_state):
        if message.text=="ارسال دوباره":
            bot.send_message(chat_id=message.chat_id, text="کد جدید برای شما ارسال شد."+"\n"+"کد جدید را وارد کنید:")
            return self.states[current_state]["nextState"]["checkRegisterCode"]
