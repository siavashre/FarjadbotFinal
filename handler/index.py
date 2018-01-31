from handler.enterCode import EnterCode
from handler.enterPhoneNumber import EnterPhoneNumber
from handler.firstTime import FirstTimeHandler

handlers = {
    "firstTime": FirstTimeHandler(),
    "enterPhoneNumber": EnterPhoneNumber(),
    "enterCode":EnterCode()
}