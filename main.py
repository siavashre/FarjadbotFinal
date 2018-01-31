from telegram.ext import Updater,CommandHandler
import json
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler

from handler.firstTime import FirstTimeHandler
from util.stateMachineRunner import StateMachineRunner

firstTime=FirstTimeHandler()
stateMachineRunner = StateMachineRunner()
botConfigs = ""
base_url="192.168.1.103"
with open("configs/bot.json","r") as f:
    botConfigs = json.load(f)

updater=Updater(botConfigs["TOKEN"])
dispatcher = updater.dispatcher

start_handler=CommandHandler('start',stateMachineRunner.process)
process_handler=MessageHandler(Filters.text | Filters.contact ,stateMachineRunner.process)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(process_handler)

updater.start_polling()
