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
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': '10',
    '11': '11',
    '12': '12'}

mounths = create_inline_kb(4, **BUTTONS)