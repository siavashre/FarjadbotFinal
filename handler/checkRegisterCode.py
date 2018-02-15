import json
from util.keyboards import keyboards
import requests
from model import setting
from model import url
class CheckRegisterCode():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def checkRegisterCode(self, bot, message, current_state):
        # print(1)
        r = requests.post(url.base_url + '/authentication/authentication-code-validator', data={'authentication_code': message.text,'phone_number': setting.phoneNumber[message.chat_id]})

        print(r.content)
        if json.loads(r.text)["is_valid"]:
            print("here")
            bot.send_message(chat_id=message.chat_id, text="برای ثبت نام مشخصات خود را وارد کنید",reply_markup=keyboards["register"])
            return self.states[current_state]["nextState"]["register"]
        else:
            print(2)
            bot.send_message(chat_id=message.chat_id, text="کد شما نادرست است"+"\n"+"لطفا دکمه ارسال مجدد را فشار دهید",reply_markup=keyboards["resendCode"])
            return self.states[current_state]["nextState"]["resnedRegisterCode"]