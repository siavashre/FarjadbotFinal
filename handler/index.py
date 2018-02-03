from handler.addBook import AddBook
from handler.enterCode import EnterCode
from handler.enterPhoneNumber import EnterPhoneNumber
from handler.firstTime import FirstTimeHandler
from handler.loggedIn import LoggedIn
from handler.resendCode import ResendCode
from handler.watchMore import WatchMore

handlers = {
    "firstTime": FirstTimeHandler(),
    "enterPhoneNumber": EnterPhoneNumber(),
    "enterCode":EnterCode(),
    "resendCode":ResendCode(),
    "loggedIn":LoggedIn(),
    "watchMore":WatchMore(),
    "addBook":AddBook()
}