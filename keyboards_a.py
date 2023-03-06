from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_enter: KeyboardButton = KeyboardButton(text='Записать')
button_history: KeyboardButton = KeyboardButton(text='История')

main_buttons: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_enter, button_history]],
                                                        resize_keyboard=True,
                                                        input_field_placeholder='сумма ; коментарий ; категоря')

button_1: KeyboardButton = KeyboardButton(text='Сегодня')
button_2: KeyboardButton = KeyboardButton(text='Вчера')
button_3: KeyboardButton = KeyboardButton(text='Неделя')
button_4: KeyboardButton = KeyboardButton(text='Месяц')

period: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1, button_2, button_3, button_4]],
                                                  one_time_keyboard=True, resize_keyboard=True)
