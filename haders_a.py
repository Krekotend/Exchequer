import datetime

from aiogram import Router
from aiogram.filters import CommandStart, Text, Command
from aiogram.types import Message, CallbackQuery
from keyboards_a import period, mounths
from posgSQL import write_users_table, show_categories_table, shows_history_day, shows_last_item, shows_history_months
from service import test_in_dig, record_notes

router: Router = Router()


def main_filter(message: Message) -> bool:
    return test_in_dig(message.text)


def date_filter(message: Message) -> bool:
    if len(message.text.split("-")) == 3:
        return True


@router.message(main_filter)
async def process_start_command(message: Message):
    record_notes(message.text, message.from_user.id)
    await message.answer(text='Понял-принял,запомнил-записал!')


@router.message(CommandStart())
async def process_start_command(message: Message):
    telega_id = (message.from_user.id,)
    name = (message.from_user.username,)
    write_users_table(name=name, telega_id=telega_id)
    await message.answer(text=f"Приветствую вас {message.from_user.username}\!\n"
                              "Я бот котороый будет запоминать ваши расходы\.\n"
                              'Запишите *сумму и коментарий* и _отправте мне_ \n'
                              'Подсказки и другие функции можно посмотреть набрав \/help или в меню',
                         parse_mode='MarkdownV2')


@router.message(date_filter)
async def process_text_endswith_bot(message: Message):
    text = ''.join([str_day + '\n' for str_day in shows_history_day(message.text, message.from_user.id)])
    total_day = f'Итого за день ' \
                f'{sum([int(i.split()[0]) for i in shows_history_day(message.text, message.from_user.id)])}'
    await message.answer(text=f'{text}\n{total_day}')


@router.message(Command(commands=['last']))
async def process_text_endswith_bot(message: Message):
    items = ''.join([f'{i[0]} - {i[1]}' + '\n' for i in shows_last_item(message.from_user.id)[::-1]])
    await message.answer(text=items)


@router.message(Command(commands=['help']))
async def show_help(message: Message):
    await message.answer(text='Что бы сделать запись нужно:\n'
                              'ввести ее в формате: \<сумма\>\ \<коментарий\>\ \<категория\>\n'
                              'пример\ _*200 бар у дяди Васи 4*_\n'
                              'Посмотреть категории можно в меню или напишите мне \/categories\n'
                              'eсли категория не выбрана он проставит ее автоматом на \'другое\' \n'
                              'В меню можно просмотреть _*Историю записей*_ или напишите мне\/history\n'
                              '_есть вопросы пишите_ \@krekotend',
                         parse_mode='MarkdownV2')


@router.message(Command(commands=['history']))
async def process_history_answer(message: Message):
    telega_id = (message.from_user.id,)
    await message.answer(text='Выберети период 👇',
                         reply_markup=period)


@router.message(Command(commands=['categories']))
async def show_categories(message: Message):
    text = ''.join([f'''{i[0]} - {i[1]}\n''' for i in show_categories_table()])
    await message.answer(text=text)


@router.message(Command(commands=['dice']))
async def cmd_dice_in_group(message: Message):
    await message.answer_dice(emoji="🎲")


@router.message(Command(commands=['contacts']))
async def show_contacts(message: Message):
    await message.answer(text='*_I will be glad to accept suggestions or wishes_*\n'
                              '||In the subject of the email\, indicate Tg\_Exchequer||\n'
                              '||Krekotend\@gmail\.com||',
                         parse_mode='MarkdownV2')


@router.callback_query(Text(text=['Сегодня']))
async def shows_today(callback: CallbackQuery):
    day = datetime.date.today()
    text = ''.join([i + '\n' for i in shows_history_day(day, callback.from_user.id)])
    total_day = f'Итого за день {sum([float(i.split()[0]) for i in shows_history_day(day, callback.from_user.id)])}'
    # if callback.message.text != 'Сегодня':
    await callback.message.edit_text(text=f'{text}\n{total_day}')

@router.callback_query(Text(text=['Вчера']))
async def shows_yesterday(callback: CallbackQuery):
    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
    text = ''.join([i + '\n' for i in shows_history_day(yesterday.date(), callback.from_user.id)])
    total_day = f'Итого за день ' \
                f'{sum([float(i.split()[0]) for i in shows_history_day(yesterday.date(), callback.from_user.id)])}'
    await callback.message.edit_text(text=f'{text}\n{total_day}')


@router.callback_query(Text(text=['Месяц']))
async def shows_mounth(callback: CallbackQuery):
    await callback.message.edit_text(text=f'Выберети месяц', reply_markup=mounths)


@router.callback_query(Text(text=['1', '3', '2', '4', '5', '6', '7', '8', '9', '10', '11', '12']))
async def shows_mounth(callback: CallbackQuery):
    month = int(callback.data)
    text = ''.join([i + '\n' for i in shows_history_months(month, callback.from_user.id)])
    total_day = f'Итого за месяц ' \
                f'{sum([float(i.split()[0]) for i in shows_history_months(month, callback.from_user.id)])}'
    await callback.message.edit_text(text=f'{text}\n{total_day}')


@router.message()
async def other(message: Message):
    await message.reply(text='Когда подружусть с ChatGPT, обязательно пойму что вы написали ,'
                             ' а пока пожалуйста пишите команды которые я понимаю')
