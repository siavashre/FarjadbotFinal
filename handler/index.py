from handler.addAdress import AddAdress
from handler.addAuthor import AddAuthor
from handler.addBook import AddBook
from handler.addCity import AddCity
from handler.addDescription import AddDescription
from handler.addEmail import AddEmail
from handler.addFamill import AddFamill
from handler.addGenre import AddGenre
from handler.addGraduate import AddGraduate
from handler.addInviteCode import AddInviteCode
from handler.addJeldNumber import AddJeldNumber
from handler.addJob import AddJob
from handler.addName import AddName
from handler.addPN import AddPN
from handler.addPageNumber import AddPageNumber
from handler.addPassword import AddPassword
from handler.addPeriod import AddPeriod
from handler.addPrice import AddPrice
from handler.addProvience import AddProvience
from handler.addReaderAge import AddReaderAge
from handler.addSummery import AddSummery
from handler.addUser import AddUser
from handler.addUserName import AddUserName
from handler.checkRegisterCode import CheckRegisterCode
from handler.enterCode import EnterCode
from handler.enterPhoneNumber import EnterPhoneNumber
from handler.firstTime import FirstTimeHandler
from handler.loggedIn import LoggedIn
from handler.register import Register
from handler.resendCode import ResendCode
from handler.resnedRegisterCode import ResendRegisterCode
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
    'addSummery':AddSummery(),
    'checkRegisterCode':CheckRegisterCode(),
    'resnedRegisterCode':ResendRegisterCode(),
    'register':Register(),
    "addUserName":AddUserName(),
    "addFamill":AddFamill(),
    "addUser":AddUser(),
    "addCity":AddCity(),
    "addProvience":AddProvience(),
    "addAdress":AddAdress(),
    "addJob":AddJob(),
    "addGraduate":AddGraduate(),
    "addInviteCode":AddInviteCode(),
    "addPN":AddPN(),
    "addPassword":AddPassword(),
    "addEmail":AddEmail()
}