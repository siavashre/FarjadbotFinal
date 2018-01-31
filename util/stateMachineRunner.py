from model.stateHistory import StateHistory
import json
import datetime, logging
from handler.index import handlers


class StateMachineRunner():
    def __init__(self):
        self.stateHistory_dict = dict()
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def process(self, bot, update):
        message = update.message
        user_stateHistories = self.get_or_make_stateHistory(message, "firstTime")
        user_stateHistories.sort(key=lambda h: h.createdAt, reverse=True)
        current_state = user_stateHistories[0].stateName
        next_stateHistory = self.run(bot, message, current_state)
        if (next_stateHistory):
            self.stateHistory_dict[message.chat_id].append(next_stateHistory)

    def run(self, bot, message, current_state):
        try:
            handler = getattr(handlers[current_state], self.states[current_state]["function"])
            next_stateName = handler(bot, message, current_state)
            if next_stateName is None:
                return None
            stateHistory = StateHistory(next_stateName, message.text, self.get_current_date_string())
            return stateHistory
        except Exception as e:
            logging.exception(":*")

    def get_or_make_stateHistory(self, message, stateName):
        currentUserHistories = self.stateHistory_dict.get(message.chat_id, None)
        stateHistory = StateHistory(stateName, message.text, self.get_current_date_string())
        if not currentUserHistories:
            self.stateHistory_dict[message.chat_id] = [stateHistory]
        return self.stateHistory_dict[message.chat_id]

    def get_current_date_string(self):
        return datetime.datetime.now()
