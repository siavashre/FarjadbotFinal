import json
from util.keyboards import keyboards
from handler import book
class AddReaderAge():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addReadAge(self, bot, message, current_state):
        readerAge={"گروه سنی الف":"A","گروه سنی ب":"B","گروه سنی ج":"C","گروه سنی د":"D","گروه سنی ه":"E"}
        book.reader_age=readerAge[message.text]
        print(book.reader_age)
        bot.send_message(chat_id=message.chat_id, text="رده سنی انتخاب شد", reply_markup=keyboards["addBook"])
        return self.states[current_state]["nextState"]["addBook"]

