import json
from util.keyboards import keyboards
import requests
from model import url
from model import setting
class ResendCode():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def resendCode(self, bot, message, current_state):
        if message.text=="ارسال دوباره":
            r = requests.post(url.base_url + '/authentication/code-checking', data={'phone': setting.phoneNumber[message.chat_id]})
            print("hoooooooooooooon")
            bot.send_message(chat_id=message.chat_id, text="کد جدید ارسال شد"+"\n"+"کد جدید را وارد کنید")
            return self.states[current_state]["nextState"]["enterCode"]
