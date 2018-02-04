import json
from util.keyboards import keyboards
from handler import book
class AddPeriod():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addPeriod(self, bot, message, current_state):
        period={"روزانه":"daily","هفتگی":"weekly","ماهانه":"monthly"}
        book.period = period[message.text]
        bot.send_message(chat_id=message.chat_id, text="مدت زمان انتخاب شد", reply_markup=keyboards["addBook"])
        return self.states[current_state]["nextState"]["addBook"]

