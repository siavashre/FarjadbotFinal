import json
from model import url
from model import setting
from util.keyboards import keyboards
import requests
class EnterCode():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def checkCode(self, bot, message, current_state):

        r = requests.post(url.base_url + '/authentication/authentication-code-validator', data={'authentication_code': message.text,'phone_number': setting.phoneNumber[message.chat_id]})

        print(r.content)
        if json.loads(r.text)["is_valid"]:
            bot.send_message(chat_id=message.chat_id, text="شما وارد حساب کاربری خورد شدید",reply_markup=keyboards["loggedIn"])
            return self.states[current_state]["nextState"]["loggedIn"]
        else:
            # print(2)
            bot.send_message(chat_id=message.chat_id, text="کد شما نادرست است"+"\n"+"لطفا دکمه ارسال مجدد را فشار دهید",reply_markup=keyboards["resendCode"])
            return self.states[current_state]["nextState"]["resendCode"]
