from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_inline_kb(width: int,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

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

    kb_builder.row(*buttons, width=width)

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