
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,Update

from telegram.ext import(
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from cread import TOKEN
from key_buttons import tele_Botton,Bottons,back
from menu import main_menu_keyboard,course_menu_keyboard

def record(update: Update, context: CallbackContext):
    text = update.message.text
    if text[:6] == 'Запись':
        print(text)
        context.bot.send_message(
            chat_id = '-877442635',
            text = text 
        )

def on_click(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="""
1. напишите сообщение.
2. напишите номер телефона.
3. выберите удобное вам время.
        """
    )

def start(update:Update, context:CallbackContext):
    context.bot.send_sticker(
        chat_id = update.effective_chat.id,
        sticker = 'CAACAgQAAxkBAAEGbYVjc3nKqLLcFDH3hN7RSbiw27ZWMQACEAEAAguHlAfQnqFnTsGTuSsE'
    ),

    update.message.reply_text(
        f"Привет! {update.effective_user.username}\nДля выбора курса выберите плитку 'Курсы'.\nВ Вкладке 'О нас' вы можете увидеть краткую информацию о нашей огранизации.\nВыбрав плитку 'Где мы' вы сможете увидеть нашу геолокацию.",
        reply_markup=main_menu_keyboard()
    ),
    
ABOUT = tele_Botton[0]
COURSE_MENU = tele_Botton[1]
GEO = tele_Botton[2]
BACK = back[0]
PYTHON = Bottons[0]
JS = Bottons[1]
UXUI = Bottons[2]
RECORD = Bottons[3]

def about(update:Update, context:CallbackContext):
    update.message.reply_text(
        "Образовательное учреждение в котором люди любого возраста за короткие сроки могут получить качественное образование в сфере IT. Основная концепция OGOGO академии это дарить знания вместе с эмоциями, развивая не только технические навыки, но и личные качества наших студентов. Целью компании является взращивание новых конкурентоспособных IT специалистов для мирового рынка компьютерных технологий.Проводим различные мероприятия для наших студентов.",
    ),

def resive_course_menu(update:Update, context:CallbackContext):
    update.message.reply_text(
        'Выберите курс:',
        reply_markup=course_menu_keyboard()
    )

def back_to_menu(update:Update, context:CallbackContext):
    update.message.reply_text(
        f"Вы вернулись в главное меню!",
        reply_markup=main_menu_keyboard()
    ),

def location(update:Update, context:CallbackContext):
    msg = context.bot.send_message(
            update.effective_chat.id,
            text = 'Location of OGOGO'
        )
    update.message.reply_location(
        #42.8735872699917, 74.61999242498408
        longitude=74.61999242498408,
        latitude=42.8735872699917,
        reply_to_message_id=msg.message_id
    )



def python_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
    [
        InlineKeyboardButton('Mentor', callback_data='python_mentor'),
        InlineKeyboardButton('Lesson', callback_data='python_lesson'),
    ],
    [InlineKeyboardButton('Price', callback_data='python_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите опцию',
        reply_markup=reply_murkup
    )


def js_inline_menu(update: Update, context: CallbackContext):
    keyboar = [
    [
        InlineKeyboardButton('Mentor', callback_data='js_mentor')
    ],
    [InlineKeyboardButton('Lesson', callback_data='js_lesson')],
    [InlineKeyboardButton('Price', callback_data='js_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboar)
    update.message.reply_text(
        'Выберите опцию',
        reply_markup=reply_murkup
    )

def UXUI_inline_menu(update: Update, context: CallbackContext):
    keyboar = [
    [
        InlineKeyboardButton('Mentor', callback_data='uxui_mentor')
    ],
    [InlineKeyboardButton('Lesson', callback_data='uxui_lesson')],
    [InlineKeyboardButton('Price', callback_data='uxui_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboar)
    update.message.reply_text(
        'Выберите опцию',
        reply_markup=reply_murkup
    )

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    keyboard = [
    [
        InlineKeyboardButton('Mentor', callback_data='python_mentor'),
        InlineKeyboardButton('Lesson', callback_data='python_lesson'),
    ],
    [InlineKeyboardButton('Price', callback_data='python_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    if query.data == 'python_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/ilias.jpg', 'rb'),
            caption = """
name: ilias
age: 16
expierence: 6 years
work place: Google, Microsoft, Facebook, Oazis
            """,
            reply_markup=reply_murkup
        )

    if query.data == 'python_price':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/mani.jpg', 'rb'),
            caption = '16000 som per month',
            reply_markup=reply_murkup
        )
    
    if query.data == 'python_lesson':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/shkila.jpg', 'rb'),
            caption ="""расписание:
                            вторник
                            четверг
                            суббота""",
            reply_markup=reply_murkup
        )
    keyboar = [
    [
        InlineKeyboardButton('Mentor', callback_data='js_mentor')
    ],
    [InlineKeyboardButton('Lesson', callback_data='js_lesson')],
    [InlineKeyboardButton('Price', callback_data='js_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboar)
    if query.data == 'js_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/jaka.jpg', 'rb'),
            caption = """
name: amir
age: 27
expierence: 10 years
work place: Tesla, Steam, Opera GX, Sham Shum, Alamedin bazar
            """,
            reply_markup=reply_murkup
        )

    if query.data == 'js_price':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/eral.jpg', 'rb'),
            caption ="""услуги:
                        vip = 26600 som,
                        obichni = 22300 som""",
            reply_markup=reply_murkup
        )
    
    if query.data == 'js_lesson':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/brutaliti.jpg', 'rb'),
            caption ="""Расписание:                       
                        понедельник
                        среда
                        пятница
                        с 18:00 до 21:00""",
            reply_markup=reply_murkup
        )
    keyboar = [
    [
        InlineKeyboardButton('Mentor', callback_data='uxui_mentor')
    ],
    [InlineKeyboardButton('Lesson', callback_data='uxui_lesson')],
    [InlineKeyboardButton('Price', callback_data='uxui_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboar)
    if query.data == 'uxui_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/dog.jpg', 'rb'),
            caption = """
name: dima
age: 35
expierence: 78 years
work place: mail.ru, gmail.com, 1000 melochei
            """,
            reply_markup=reply_murkup
        )

    if query.data == 'uxui_price':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/dogi.jpg', 'rb'),
            caption ="""услуги:
                        vip = 26600 som,
                        obichni = 22300 som
                        разноплановые = 500к в секунду""",
            reply_markup=reply_murkup
                        
        )
    
    if query.data == 'uxui_lesson':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/kit.jpg', 'rb'),
            caption ="""Расписание:                       
                        понедельник
                        вторник
                        среда
                        четверг
                        пятница
                        с 18:00 до 21:00""",
            reply_markup=reply_murkup
        )


def buteron(update: Update, context: CallbackContext):
    quer = update.callback_query
    


def buter(update: Update, context: CallbackContext):
    quer = update.callback_query
   


updater = Updater(TOKEN,persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start',start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    back_to_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE_MENU),
    resive_course_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT),
    about
))



updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON),
    python_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JS),
    js_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(UXUI),
    UXUI_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(GEO),
    location
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(RECORD),
    on_click
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    record
))


updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()