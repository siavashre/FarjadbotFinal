import telegram

keyboards = {
    "enterPhoneNumber": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("به اشتراک گذاری شماره تلفن", request_contact=True)
        ]
    ], resize_keyboard=True),
    "loggedIn": telegram.ReplyKeyboardMarkup([

        [telegram.KeyboardButton("اضافه کردن کتاب"), telegram.KeyboardButton("مشاهده کتب")],
        [telegram.KeyboardButton("دعوت از دوستان")]

    ], resize_keyboard=True),
    "resendCode": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("ارسال دوباره")
        ]
    ], resize_keyboard=True),
    "watchBook": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("مشاهده کتب")
        ]
    ], resize_keyboard=True),
    "watchMore": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("مشاهده بیشتر"),
            telegram.KeyboardButton("بازگشت")
        ]
    ], resize_keyboard=True),
    "addBook": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("اضافه کن"),
            telegram.KeyboardButton("بازگشت"),
            telegram.KeyboardButton("عنوان*")
        ],
        [telegram.KeyboardButton("نویسنده*"),
         telegram.KeyboardButton("قیمت*"),
         telegram.KeyboardButton("مدت زمان*")],
        [telegram.KeyboardButton("ژانر"),
         telegram.KeyboardButton("رده سنی"),
         telegram.KeyboardButton("تعداد صفحات")],
        [telegram.KeyboardButton("تعداد جلد"),
         telegram.KeyboardButton("خلاصه کتاب"),
         telegram.KeyboardButton("توضیحات"), ]
    ], resize_keyboard=True)
    ,
    "addGenre": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("وحشت"),
            telegram.KeyboardButton("ماجراجویی"),
            telegram.KeyboardButton("کمدی"), ], [
            telegram.KeyboardButton("تاریخی"),
            telegram.KeyboardButton("افسانه"),
            telegram.KeyboardButton("هنری"), ], [
            telegram.KeyboardButton("روانشناسی"),
            telegram.KeyboardButton("عاشقانه"),
            telegram.KeyboardButton("ورزشی"),
            telegram.KeyboardButton("تراژدی"),
        ]
    ], resize_keyboard=True)
    ,
    "addReadeAge": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("گروه سنی الف"),
            telegram.KeyboardButton("گروه سنی ب"),
            telegram.KeyboardButton("گروه سنی ج"), ], [
            telegram.KeyboardButton("گروه سنی د"),
            telegram.KeyboardButton("گروه سنی ه")
        ]
    ], resize_keyboard=True)
    ,
    "addPeriod": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("روزانه"),
            telegram.KeyboardButton("هفتگی"),
            telegram.KeyboardButton("ماهانه"), ]
    ], resize_keyboard=True),
    "graduation": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("زیر دیپلم"),
            telegram.KeyboardButton("ٔدیپلم"),
            telegram.KeyboardButton("کارشناسی"), ], [
            telegram.KeyboardButton("کارشناسی ارشد"),
            telegram.KeyboardButton("دکتری")
        ]
    ], resize_keyboard=True)
    ,
    "register": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("نام"),
            telegram.KeyboardButton("نام خانوادگی"),
            telegram.KeyboardButton("نام کاربری")
        ],
        [telegram.KeyboardButton("گذرواژه"),
         telegram.KeyboardButton("ایمیل"),
         telegram.KeyboardButton("شهر")],
        [telegram.KeyboardButton("استان"),
         telegram.KeyboardButton("آدرس"),
         telegram.KeyboardButton("شغل")],
        [telegram.KeyboardButton("تحصیلات"),
         telegram.KeyboardButton("کد دعوت"),
         telegram.KeyboardButton("ثبت نام"),
         telegram.KeyboardButton("بازگشت"),
         ]
    ], resize_keyboard=True)

}
