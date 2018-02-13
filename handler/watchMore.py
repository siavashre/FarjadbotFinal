import json
from util.keyboards import keyboards
from model import setting
class WatchMore():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def watchMore(self, bot, message, current_state):
        genre = {'Horror': 'وحشت', 'Adventure': "ماجراجویی", 'Comedy': 'کمدی', "Historical"
        : "تاریخی", "Fantasy": "فانتزی", "Art": "هنری", "Psychology": "روانشناسی", "Romance": "عاشقانه",
                 "Sports": "ورزشی"
            , "Trajedy": "تراژدی"}
        readerAge = {"A": "گروه سنی الف", "B": "گروه سنی ب", "C": "گروه سنی ج", "D": "گروه سنی د", "E": "گروه سنی ه"}
        period = {"daily": "روزانه", "weekly": "هفتگی", "monthly": "ماهانه"}
        if message.text=="مشاهده بیشتر":
            if (setting.counter*5>= len(setting.books)):
                bot.send_message(chat_id=message.chat_id, text="کتاب دیگری موجود نیست",reply_markup=keyboards["watchMore"])

                return self.states[current_state]["nextState"]["watchMore"]
            elif((setting.counter+1)*5<len(setting.books)):
                setting.counter=setting.counter+1
                books = setting.books[setting.counter*5:setting.counter*5+5]
                for book in books:
                    bot.send_message(chat_id=message.chat_id, text=
                    "عنوان:" + book['title'] + "\n"
                    + "نویسنده:" + book['author'] + "\n"
                    + "سال انتشار:" + str(book['pub_date']) + "\n"
                    + "مدت زمان:" + period[book['period']] + "\n"
                    + "قیمت:" + str(book['price']) + "\n"
                    + "ژانر:" + genre[book['genre']] + "\n"
                    + "رده سنی:" + readerAge[book['reader_age']] + "\n"
                    + "خلاصه:" + book['summary'] + "\n"
                    + "توضیحات:" + book['description'] + "\n"
                    + "تعداد جلد:" + str(book['jeld_num']) + "\n"
                    + "تعداد صفحه:" + str(book['page_num'])
                                     , reply_markup=keyboards["watchMore"])
                setting.counter=setting.counter+1
                return self.states[current_state]["nextState"]["watchMore"]
            else:
                books = setting.books[setting.counter * 5:len(setting.books)]
                for book in books:
                    bot.send_message(chat_id=message.chat_id, text=
                    "عنوان:" + book['title'] + "\n"
                    + "نویسنده:" + book['author'] + "\n"
                    + "سال انتشار:" + str(book['pub_date']) + "\n"
                    + "مدت زمان:" + period[book['period']] + "\n"
                    + "قیمت:" + str(book['price']) + "\n"
                    + "ژانر:" + genre[book['genre']] + "\n"
                    + "رده سنی:" + readerAge[book['reader_age']] + "\n"
                    + "خلاصه:" + book['summary'] + "\n"
                    + "توضیحات:" + book['description'] + "\n"
                    + "تعداد جلد:" + str(book['jeld_num']) + "\n"
                    + "تعداد صفحه:" + str(book['page_num'])
                                     , reply_markup=keyboards["watchMore"])
                setting.counter=setting.counter+1
                return self.states[current_state]["nextState"]["watchMore"]





            # return self.states[current_state]["nextState"]["watchMore"]
        elif message.text=="بازگشت":
            bot.send_message(chat_id=message.chat_id, text="شما در صفحه اصلی هستید",reply_markup=keyboards["loggedIn"])
            return self.states[current_state]["nextState"]["loggedIn"]
