import telegram
from key_buttons import tele_Botton,Bottons,back

def main_menu_keyboard():
    keyboard = ([
        [telegram.KeyboardButton(tele_Botton[1])],
        [telegram.KeyboardButton(tele_Botton[0])],
        [telegram.KeyboardButton(tele_Botton[2])],
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )

def course_menu_keyboard():
    keyboard = ([
        [telegram.KeyboardButton(Bottons[0])],
        [telegram.KeyboardButton(Bottons[1])],
        [telegram.KeyboardButton(Bottons[2])],
        [telegram.KeyboardButton(back[0])],
        [telegram.KeyboardButton(Bottons[3])],
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )