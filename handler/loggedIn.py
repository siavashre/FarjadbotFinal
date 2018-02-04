import json
from util.keyboards import keyboards
import requests
from model import url
class LoggedIn():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def loggedIn(self, bot, message, current_state):
        if message.text=="Add Book to your account":
            print("aaa")
            bot.send_message(chat_id=message.chat_id, text="لطفا هر فیلد را انتخاب و وارد کنید",reply_markup=keyboards["addBook"])
            return self.states[current_state]["nextState"]["addBook"]
        elif message.text=="Whatch Books":
            r = requests.get(url.base_url + '/books/api/')
            print(r.content)
            bot.send_message(chat_id=message.chat_id,text=str(r))
            # ketab behesh bedim
            print("bbbb")
            # bot.send_message(chat_id=message.chat_id, text="Hold button for watch books",reply_markup=keyboards["watchBook"])
            bot.send_message(chat_id=message.chat_id,text="moad",
                             reply_markup=keyboards["watchMore"])
            return self.states[current_state]["nextState"]["watchMore"]
