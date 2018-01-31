import json
import requests
from model import url
class EnterPhoneNumber():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def checkPhoneNumber(self, bot, message, current_state):
        # if msg.contact.user_id != msg.chat_id
        # check kardan e in ke oke ya na
        # base_url = "http://192.168.1.101:8000"
        phoneNumber=''
        if message.text == None :
            # bot.send_message(chat_id=message.chat_id, text=message.text)
            phoneNumber = message['contact']['phone_number']
            phoneNumber ='0'+ phoneNumber[2:]
        else:
            # bot.send_message(chat_id=message.chat_id, text=message['contact']['phone_number'])
            phoneNumber = message.text
        print(phoneNumber)
        # r=requests.post(url.base_url+'/api/phone-validator/',data={'phone_number':phoneNumber})
        # print(r.text)
        # print(r.content)
        # print(json.loads(r.text)['existence'])
        # --------------------
        # if json.loads(r.text)['existence'] :
        #     bot.send_message(chat_id=message.chat_id, text="Dear" +json.loads(r.text)['name']+ "Please Enter Your Code")
        return self.states[current_state]["nextState"]["enterCode"]
        # else:
        #     bot.send_message(chat_id=message.chat_id, text="Please Register On site")
        #     return self.states[current_state]["nextState"]["firstTime"]


