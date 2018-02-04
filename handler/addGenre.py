import json
from util.keyboards import keyboards
from handler import book


class AddGenre():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addGenre(self, bot, message, current_state):
        genre = {'وحشت': 'Horror', 'ماجراجویی': "Adventure", 'کمدی': 'Comedy', "تاریخی"
        : "Historical", "افسانه": "Fantasy", "هنری": "Art", "روانشناسی": "Psychology", "عاشقانه": "Romance",
                 "ورزشی": "Sports"
            , "تراژدی": "Trajedy"}
        book.genre = genre[message.text]
        bot.send_message(chat_id=message.chat_id, text="ژانر انتخاب شد", reply_markup=keyboards["addBook"])
        return self.states[current_state]["nextState"]["addBook"]
