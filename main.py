from telegram.ext import Updater,CommandHandler
import json
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
import time

from handler.firstTime import FirstTimeHandler
from util.stateMachineRunner import StateMachineRunner

firstTime=FirstTimeHandler()
stateMachineRunner = StateMachineRunner()
botConfigs = ""
with open("configs/bot.json","r") as f:
    botConfigs = json.load(f)

updater=Updater(botConfigs["TOKEN"])
dispatcher = updater.dispatcher

start_handler=CommandHandler('start',stateMachineRunner.process)
process_handler=MessageHandler(Filters.text | Filters.contact ,stateMachineRunner.process)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(process_handler)

while True:
    try:
        updater.start_polling()
    except Exception as e:
        time.sleep(15)

