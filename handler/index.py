from handler.addAuthor import AddAuthor
from handler.addBook import AddBook
from handler.addDescription import AddDescription
from handler.addGenre import AddGenre
from handler.addJeldNumber import AddJeldNumber
from handler.addName import AddName
from handler.addPageNumber import AddPageNumber
from handler.addPeriod import AddPeriod
from handler.addPrice import AddPrice
from handler.addReaderAge import AddReaderAge
from handler.addSummery import AddSummery
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
    "addBook":AddBook(),
    'addName':AddName(),
    "addAuthor":AddAuthor(),
    "addPrice":AddPrice(),
    "addPeriod":AddPeriod(),
    'addDescription':AddDescription(),
    'addGenre':AddGenre(),
    'addJeldNumber':AddJeldNumber(),
    'addPageNumber':AddPageNumber(),
    'addReadAge':AddReaderAge(),
    'addSummery':AddSummery()
}