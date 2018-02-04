import json
import requests
from model import url
from model import tokens
from util.keyboards import keyboards
from handler import book
class AddBook():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)
    def setName(self,name):
        self.name=name
    def printBook(self):
        print(book.name)
        print(book.author)
        print(book.description)
        print(book.genre)
        print(book.jeld_num)
        print(book.page_num)
        print(book.period)
        print(book.price)
        print(book.summery)
        print(book.reader_age)
    def addBook(self, bot, message, current_state):
        if message.text=="عنوان*":
            bot.send_message(chat_id=message.chat_id, text="نام کتاب را وارد کنید")
            return self.states[current_state]["nextState"]["addName"]
        elif message.text=="نویسنده*":
            bot.send_message(chat_id=message.chat_id, text="نام نویسنده را وارد کنید")
            return self.states[current_state]["nextState"]["addAuthor"]
        elif message.text=="قیمت*":
            bot.send_message(chat_id=message.chat_id, text="قیمت را به تومان وارد کنید")
            return self.states[current_state]["nextState"]["addPrice"]
        elif message.text=="مدت زمان*":
            bot.send_message(chat_id=message.chat_id, text="زمان وارد کن",reply_markup=keyboards["addPeriod"])
            return self.states[current_state]["nextState"]["addPeriod"]
        elif message.text=="تعداد صفحات":
            bot.send_message(chat_id=message.chat_id, text="تعداد صفحات را وارد کن")
            return self.states[current_state]["nextState"]["addPageNumber"]
        elif message.text=="رده سنی":
            bot.send_message(chat_id=message.chat_id, text="رده سنی را وارد کن",reply_markup=keyboards["addReadeAge"])
            return self.states[current_state]["nextState"]["addReadAge"]
        elif message.text=="ژانر":
            bot.send_message(chat_id=message.chat_id, text="ژانر را انتخاب کن",reply_markup=keyboards["addGenre"])
            return self.states[current_state]["nextState"]["addGenre"]
        elif message.text=="تعداد جلد":
            bot.send_message(chat_id=message.chat_id, text="تعداد جلد راوارد کن")
            return self.states[current_state]["nextState"]["addJeldNumber"]
        elif message.text=="توضیحات":
            bot.send_message(chat_id=message.chat_id, text="توضیحات را وارد کن")
            return self.states[current_state]["nextState"]["addDescription"]
        elif message.text=="خلاصه کتاب":
            bot.send_message(chat_id=message.chat_id, text="خلاصه کتاب را وارد کن")
            return self.states[current_state]["nextState"]["addSummery"]
        elif message.text=="بازگشت":
            bot.send_message(chat_id=message.chat_id, text="به صفحه اصلی بازگشتید", reply_markup=keyboards["loggedIn"])
            return self.states[current_state]["nextState"]["loggedIn"]
        elif message.text=="اضافه کن":
            # اضافه کردن کتاب
            if book.name=="" or book.author=="" or book.price==0 or book.period=="":
                bot.send_message(chat_id=message.chat_id, text="لطفا فیلد های ستاره دار را وارد کنید")
                return self.states[current_state]["nextState"]["addBook"]
            else:
                r = requests.post(url.base_url + '/books/api/create/', data={'token':tokens.tokens[message.chat_id],'title':book.name,'author':book.author
                                                                                ,'period':book.period,"price":book.price
                                                                                ,"genre":book.genre,'reader_age':book.reader_age,
                                                                                'summary':book.summery,'description':book.description,
                                                                                'jeld_num':book.jeld_num,'page_num':book.page_num,'length':20,'width':10,'pub_date':"1999-12-12"})
                print(r.text)
                bot.send_message(chat_id=message.chat_id, text="کتاب شما با موفقیت اضافه شد",reply_markup=keyboards["loggedIn"])
                book.printBook()
                book.eraseBook()
                return self.states[current_state]["nextState"]["loggedIn"]


