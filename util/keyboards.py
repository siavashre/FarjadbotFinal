import telegram

keyboards = {
    "enterPhoneNumber": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("Share Phone Number", request_contact=True)
        ]
    ], resize_keyboard=True),
    "loggedIn": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("Add Book to your account"), telegram.KeyboardButton("Whatch Books")
        ]
    ], resize_keyboard=True),
    "resendCode": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("Resend Code")
        ]
    ], resize_keyboard=True),
    "watchBook": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("Watch books")
        ]
    ], resize_keyboard=True),
    "watchMore": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("Watch More"),
            telegram.KeyboardButton("Return")
        ]
    ], resize_keyboard=True),
    "addBook": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("اضافه کن"),
            telegram.KeyboardButton("بازگشت"),
            telegram.KeyboardButton("عنوان")
        ],
        [telegram.KeyboardButton("نویسنده"),
         telegram.KeyboardButton("قیمت"),
         telegram.KeyboardButton("مدت زمان")],
        [telegram.KeyboardButton("ژانر"),
         telegram.KeyboardButton("رده سنی"),
         telegram.KeyboardButton("تعداد صفحات")],
        [telegram.KeyboardButton("تعداد جلد"),
         telegram.KeyboardButton("خلاصه کتاب"),
         telegram.KeyboardButton("توضیحات"), ]
    ], resize_keyboard=True)

}
