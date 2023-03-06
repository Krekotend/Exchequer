import datetime

from aiogram import Router
from aiogram.filters import CommandStart, Text, Command
from aiogram.types import Message
from keyboards_a import main_buttons, period
from posgSQL import write_users_table, write_data_table, show_categories_table, shows_history_day, shows_last_item

router: Router = Router()


def main_filter(message: Message) -> bool:
    if len(message.text.split(";")) == 3:
        mas = message.text.split(";")  # перенести в блок с функциями-обработчиками (создать)
        mas_2 = mas[2]
        if len(mas[2]) == 0:
            mas_2 = 11
        main_info = (int(mas[0]), mas[1], mas_2)
        write_data_table(*main_info, message.from_user.id)
        return True


def date_filter(message: Message) -> bool:
    if len(message.text.split("-")) == 3:
        return True


@router.message(main_filter)
async def process_start_command(message: Message):
    await message.answer(text='Понял-принял,запомнил-записал!')


@router.message(CommandStart())
async def process_start_command(message: Message):
    telega_id = (message.from_user.id,)
    name = (message.from_user.username,)
    write_users_table(name=name, telega_id=telega_id)
    await message.answer(text=f"Приветствую вас {message.from_user.username}!\n"
                              "Что вы хотите сделать ?", reply_markup=main_buttons)


@router.message(date_filter)
async def process_text_endswith_bot(message: Message):
    text = ''.join([i + '\n' for i in shows_history_day(message.text, message.from_user.id)])
    total_day = f'Итого за день {sum([int(i.split()[0]) for i in shows_history_day(message.text, message.from_user.id)])}'
    await message.answer(text=f'{text}\n{total_day}')


@router.message(Text('Кат'))
async def process_text_endswith_bot(message: Message):
    text = ''.join([i + '\n' for i in show_categories_table()])
    await message.answer(text=text)


@router.message(Command(commands=['last']))
async def process_text_endswith_bot(message: Message):
    items = ''.join([f'{i[0]} - {i[1]}' + '\n' for i in shows_last_item(message.from_user.id)[::-1]])
    await message.answer(text=items)

@router.message(Command(commands=['help']))
async def help(message: Message):
    await message.answer(text='Что бы сделать запись нужно:\n'
                                   'ввести ее в формате \<сумма\>\;\<коментарий\>\;\<категория\>\n'
                              'между значениями обязательно проставти ➡ знак *_  ;  _*\n'
                              'если форма записи не удобна или есть предложения напишите мне \n'
                                   'пример\ _*200; бар у дяди Васи \; 4*_\n'
                                   'что бы посмотреть какие есть категории напишите в чат слово _*\\"Кат\\"*_\n'
                                   'если категория не выбрана он проставит ее автоматом на другое \n'
                              'есть вопросы пишите \@krekotend',
                              parse_mode='MarkdownV2')


@router.message(Command(commands=['dice']))
async def cmd_dice_in_group(message: Message):
    await message.answer_dice(emoji="🎲")


@router.message(Command(commands=['contacts']))
async def cmd_dice_in_group(message: Message):
    await message.answer(text='*_I will be glad to accept suggestions or wishes_*\n'
                              '||In the subject of the email\, indicate Tg\_Exchequer||\n'
                              '||Krekotend\@gmail\.com||',
                         parse_mode='MarkdownV2')


@router.message(Text('Записать'))
async def process_entry_answer(message: Message):
    await message.answer(text='Запишите текст в формате: \n*сумма ; коментарий ; категория*\n'
                              '*ВАЖНО* разделитель между значениями должен быть ➡*_  ;  _*\n'
                              'Вы можете не заплнить категорию, но поставте ➡*_  ;  _*\n '
                              '_Отправте мне, а я запомню _ 🤓🧮 ',
                         parse_mode='MarkdownV2')


@router.message(Text('История'))
async def process_history_answer(message: Message):
    telega_id = (message.from_user.id,)
    await message.answer(text='Выберети период 👇',
                         reply_markup=period)


@router.message(Text('Сегодня'))
async def shows_today(message: Message):
    day = datetime.date.today()
    text = ''.join([i + '\n' for i in shows_history_day(day, message.from_user.id)])
    total_day = f'Итого за день {sum([int(i.split()[0]) for i in shows_history_day(day, message.from_user.id)])}'
    await message.answer(text=f'{text}\n{total_day}', reply_markup=main_buttons)


@router.message(Text('Вчера'))
async def shows_today(message: Message):
    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
    text = ''.join([i + '\n' for i in shows_history_day(yesterday.date(), message.from_user.id)])
    total_day = f'Итого за день {sum([int(i.split()[0]) for i in shows_history_day(yesterday.date(), message.from_user.id)])}'
    await message.answer(text=f'{text}\n{total_day}', reply_markup=main_buttons)


@router.message()
async def other(message: Message):
    await message.reply(text='Когда подружусть с ChatGPT, обязательно пойму что вы написали ,'
                             ' а пока пожалуйста пишите команды которые я понимаю')
