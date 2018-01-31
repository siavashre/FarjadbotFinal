import json

class EnterCode():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def checkCode(self, bot, message, current_state):
        bot.send_message(chat_id=message.chat_id, text="hahahaha")
        return self.states[current_state]["nextState"]["resendCode"]
