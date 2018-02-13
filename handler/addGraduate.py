import json
from util.keyboards import keyboards
from handler import user
class AddGraduate():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def addGraduate(self, bot, message, current_state):
        user.graduation=message.text
        print("kri")
        bot.send_message(chat_id=message.chat_id, text="تحصیلات انتخاب شد", reply_markup=keyboards['register'])
        return self.states[current_state]["nextState"]["register"]

