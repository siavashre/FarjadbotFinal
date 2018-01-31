import telegram

keyboards = {
    "enterPhoneNumber": telegram.ReplyKeyboardMarkup([
        [
            telegram.KeyboardButton("Share Phone Number", request_contact=True)
        ]
    ], resize_keyboard=True)
}