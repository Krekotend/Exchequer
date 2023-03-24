from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
# button_1: KeyboardButton = KeyboardButton(text='Сегодня')
# button_2: KeyboardButton = KeyboardButton(text='Вчера')
# button_3: KeyboardButton = KeyboardButton(text='Месяц')
# button_4: KeyboardButton = KeyboardButton(text='Другое')
#
# period: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1, button_2, button_3, button_4]],
#                                                    resize_keyboard=True,one_time_keyboard=True)
#
# period: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1, button_2, button_3, button_4]],
#                                                    resize_keyboard=True,one_time_keyboard=True)
#
# aiogram_calendar
# Функция для генерации инлайн-клавиатур "на лету"
def create_inline_kb(width: int,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=button ,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()



today_button: InlineKeyboardButton = InlineKeyboardButton(
    text='Сегодня',
    callback_data='Сегодня')

yearstuday_button: InlineKeyboardButton = InlineKeyboardButton(
    text='Вчера',
    callback_data='Вчера')

mounth_button: InlineKeyboardButton = InlineKeyboardButton(
    text='Месяц',
    callback_data='Месяц')

period: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[today_button],
                     [yearstuday_button],[mounth_button]])

BUTTONS: dict[str, str] = {
    '1': '1',
    '2': '2',
    '3': '3',
    'btn_4': '4',
    'btn_5': '5',
    'btn_6': '6',
    'btn_7': '7',
    'btn_8': '8',
    'btn_9': '9',
    'btn_10': '10',
    'btn_11': '11',
    'btn_12': '12'}

mounths = create_inline_kb(4, **BUTTONS)