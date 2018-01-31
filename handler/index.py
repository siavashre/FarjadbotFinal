from handler.enterCode import EnterCode
from handler.enterPhoneNumber import EnterPhoneNumber
from handler.firstTime import FirstTimeHandler
from handler.resendCode import ResendCode

handlers = {
    "firstTime": FirstTimeHandler(),
    "enterPhoneNumber": EnterPhoneNumber(),
    "enterCode":EnterCode(),
    "resendCode":ResendCode()
}