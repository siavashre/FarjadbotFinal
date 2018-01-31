import telegram

keyboards = {
    "enterPhoneNumber": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("Share Phone Number", request_contact=True)
        ]
    ], resize_keyboard=True),
    "addBook":telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("Add Book to your account"),telegram.KeyboardButton("Whatch Your Book")
        ]
    ], resize_keyboard=True),
    "resendCode": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("Resend Code")
        ]
    ], resize_keyboard=True)
}