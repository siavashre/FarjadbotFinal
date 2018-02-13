import json
import requests
from model import url
from model import tokens
from util.keyboards import keyboards
from handler import user


class Register():
    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def setName(self, name):
        self.name = name

    def register(self, bot, message, current_state):
        if message.text == "نام":
            bot.send_message(chat_id=message.chat_id, text="نام خود را وارد کنید")
            return self.states[current_state]["nextState"]["addUserName"]
        elif message.text == "نام خانوادگی":
            bot.send_message(chat_id=message.chat_id, text="نام خانوادگی خود را وارد کنید")
            return self.states[current_state]["nextState"]["addFamill"]
        elif message.text == "نام کاربری":
            bot.send_message(chat_id=message.chat_id, text="نام کاربری خود را به انگلیسی وارد کنید")
            return self.states[current_state]["nextState"]["addUser"]
        elif message.text == "گذرواژه":
            bot.send_message(chat_id=message.chat_id, text="گذرواژه خود را وارد کنید")
            return self.states[current_state]["nextState"]["addPassword"]
        elif message.text == "شهر":
            bot.send_message(chat_id=message.chat_id, text="شهر خود را وارد کنید")
            return self.states[current_state]["nextState"]["addCity"]
        elif message.text == "استان":
            bot.send_message(chat_id=message.chat_id, text="استان خود را وارد کنید")
            return self.states[current_state]["nextState"]["addProvience"]
        elif message.text == "آدرس":
            bot.send_message(chat_id=message.chat_id, text="آدرس خود را وارد کنید")
            return self.states[current_state]["nextState"]["addAdress"]
        elif message.text == "شغل":
            bot.send_message(chat_id=message.chat_id, text="شغل خود را وارد کنید")
            return self.states[current_state]["nextState"]["addJob"]
        elif message.text == "کد دعوت":
            bot.send_message(chat_id=message.chat_id, text="در صورت وجود کد دعوت خود را وارد کنید")
            return self.states[current_state]["nextState"]["addInviteCode"]
        elif message.text == "تحصیلات":
            bot.send_message(chat_id=message.chat_id, text="تحصیلات خود را انتخاب کنید",reply_markup=keyboards['graduation'])
            return self.states[current_state]["nextState"]["addGraduate"]
        elif message.text == "ایمیل":
            bot.send_message(chat_id=message.chat_id, text="ایمیل خود را وارد کنید")
            return self.states[current_state]["nextState"]["addEmail"]
        elif message.text == "بازگشت":
            bot.send_message(chat_id=message.chat_id, text="به صفحه اصلی بازگشتید",reply_markup=keyboards['enterPhoneNumber'])
            return self.states[current_state]["nextState"]["firstTime"]
        elif message.text == "ثبت نام":
            print(user.name)
            print(user.famil)
            print(user.passwrod)
            print(user.email)
            print(user.city)
            print(user.provience)
            print(user.phoneNumber)
            print(user.graduation)
            print(user.inviteCode)
            print(user.username)
            print(user.job)
            bot.send_message(chat_id=message.chat_id, text="به صفحه اصلی بازگشتید",reply_markup=keyboards['loggedIn'])

            return self.states[current_state]["nextState"]["loggedIn"]
            # اضافه کردن کتاب
            # if book.name == "" or book.author == "" or book.price == 0 or book.period == "":
            #     bot.send_message(chat_id=message.chat_id, text="لطفا فیلد های ستاره دار را وارد کنید")
            #     return self.states[current_state]["nextState"]["addBook"]
            # else:
            #     r = requests.post(url.base_url + '/books/api/create/',
            #                       data={'token': tokens.tokens[message.chat_id], 'title': book.name,
            #                             'author': book.author
            #                           , 'period': book.period, "price": book.price
            #                           , "genre": book.genre, 'reader_age': book.reader_age,
            #                             'summary': book.summery, 'description': book.description,
            #                             'jeld_num': book.jeld_num, 'page_num': book.page_num, 'length': 20, 'width': 10,
            #                             'pub_date': "1999-12-12"})
            #     print(r.text)
            #     if json.loads(r.text)['book_pk'] == 0:
            #         bot.send_message(chat_id=message.chat_id, text="کتاب شما اضافه نشد. بار دیگر تلاش کنید",
            #                          reply_markup=keyboards["loggedIn"])
            #         return self.states[current_state]["nextState"]["loggedIn"]
            #     else:
            #         bot.send_message(chat_id=message.chat_id, text="کتاب شما با موفقیت اضافه شد",
            #                          reply_markup=keyboards["loggedIn"])
            #         print(r.text)
            #         book.printBook()
            #         book.eraseBook()
            #         return self.states[current_state]["nextState"]["loggedIn"]
