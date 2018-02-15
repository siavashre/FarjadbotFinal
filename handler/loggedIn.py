import json
from util.keyboards import keyboards
import requests
import ast
from model import url
from model import setting
from model import tokens

class LoggedIn():

    def __init__(self):
        with open('configs/states.json', 'r') as f:
            self.states = json.load(f)

    def loggedIn(self, bot, message, current_state):
        genre = {'Horror': 'وحشت', 'Adventure': "ماجراجویی", 'Comedy': 'کمدی', "Historical"
        : "تاریخی", "Fantasy": "فانتزی", "Art": "هنری", "Psychology": "روانشناسی", "Romance": "عاشقانه",
                 "Sports": "ورزشی"
            , "Trajedy": "تراژدی"}
        readerAge = { "A":"گروه سنی الف",  "B":"گروه سنی ب",  "C":"گروه سنی ج",  "D":"گروه سنی د",  "E":"گروه سنی ه"}
        period = { "daily":"روزانه",  "weekly":"هفتگی",  "monthly":"ماهانه"}
        if message.text=="اضافه کردن کتاب":
            print("aaa")
            bot.send_message(chat_id=message.chat_id, text="لطفا هر فیلد را انتخاب و وارد کنید",reply_markup=keyboards["addBook"])
            return self.states[current_state]["nextState"]["addBook"]
        elif message.text=="مشاهده کتب":
            setting.counter = 0
            r = requests.get(url.base_url + '/books/api/')
            print(r.text)
            books=ast.literal_eval(r.text)
            setting.books=books
            print(books)
            books=books[0:5]
            for book in books:
                bot.send_message(chat_id=message.chat_id, text=
                                 "عنوان:"+book['title']+"\n"
                                 +"نویسنده:"+book['author']+"\n"
                                 +"سال انتشار:"+str(book['pub_date'])+"\n"
                                 +"مدت زمان:"+period[book['period']]+"\n"
                                 +"قیمت:"+str(book['price'])+"\n"
                                 +"ژانر:"+genre[book['genre']]+"\n"
                                 +"رده سنی:"+readerAge[book['reader_age']]+"\n"
                                 +"خلاصه:"+book['summary']+"\n"
                                 +"توضیحات:"+book['description']+"\n"
                                 +"تعداد جلد:"+str(book['jeld_num'])+"\n"
                                 +"تعداد صفحه:"+str(book['page_num'])
                                 ,reply_markup=keyboards["watchMore"])
            return self.states[current_state]["nextState"]["watchMore"]
        elif message.text == "دعوت از دوستان":
            r = requests.post(url.base_url + '/api/invitation-code-generate/',data={'phone_number':setting.phoneNumber[message.chat_id]})
            print(r.content)
            bot.send_message(chat_id=message.chat_id, text="کد دعوت شما به صورت زیر است"+"\n"+json.loads(r.text)['invitation_code']+"\n"+json.loads(r.text)['error'])
            return self.states[current_state]["nextState"]["loggedIn"]



