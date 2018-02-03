import json
from util.keyboards import keyboards
class AddBook():
    name=""
    author=""
    price=0
    period=""
    page_num=0
    genre=""
    reader_age=""
    jeld_num=0
    summery=""
    description=""

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addBook(self, bot, message, current_state):
        if message.text=="عنوان":
            bot.send_message(chat_id=message.chat_id, text="نام کتاب را وارد کنید")
            self.name=message.text
            print(self.name)
            # return self.states[current_state]["nextState"]["watchMore"]