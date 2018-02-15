import json
import requests
from model import url
from model import tokens
from model import setting
from util.keyboards import keyboards
class EnterPhoneNumber():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def checkPhoneNumber(self, bot, message, current_state):
        phoneNumber=''
        if message.text == None :
            phoneNumber = message['contact']['phone_number']
            phoneNumber ='0'+ phoneNumber[2:]
        else:
            phoneNumber = message.text
        print(phoneNumber)
        r=requests.post(url.base_url+'/api/phone-validator/',data={'phone_number':phoneNumber})
        if json.loads(r.text)['existence'] :
            bot.send_message(chat_id=message.chat_id, text=json.loads(r.text)['name']+" عزیز"+ "کد ارسال شده به تلفن همراه خود را وارد کنید")
            tokens.tokens.update({message.chat_id:json.loads(r.text)['token']})
            print(tokens.tokens)
            setting.phoneNumber.update({message.chat_id: phoneNumber})

            r = requests.post(url.base_url + '/authentication/code-checking',data={'phone': phoneNumber})
            print("aaa")
            print(r.content)
            return self.states[current_state]["nextState"]["enterCode"]
        else:
            setting.phoneNumber.update({message.chat_id:phoneNumber})
            print("qwer")
            r = requests.post(url.base_url + '/authentication/code-checking', data={'phone': phoneNumber})
            print(r.content)
            print("hbbbb")
            bot.send_message(chat_id=message.chat_id, text="شما در سایت ما ثبت نام نکرده اید.\n برای ثبت نام کد ارسال شده به تلفن همراه خود را وارد کنید",reply_markup=keyboards["resendCode"])
            return self.states[current_state]["nextState"]["checkRegisterCode"]


