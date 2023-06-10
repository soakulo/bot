from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import (CallbackQuery, KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.callback_data import CallbackData
API_TOKEN: str = '5783789469:AAEreVKLZID1SPhgg1Ym6Bog4m24OM9767c'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)

cb = CallbackData('keyboard', 'action')

data = {
    1 : 500,
    2: 600,
    3: 450,
    4: 300,
    5: None
}
names = ['Фуагра', 'Пицца "Маргарита"', 'Паста с креветками', 'Чизкейк Нью-Йорк', 'Конец заказа']
buttons = list()
number = -1
push = 0
for i in range(len(names)):
    button = InlineKeyboardButton(text=names[number+1], callback_data=str(push+1))
    number +=1
    push += 1
    buttons.append(button)

keyboard = InlineKeyboardMarkup(row_width=2)
keyboard.add(*buttons)

@dp.message_handler(CommandStart())
async def process_start_command(message):
    keyboard0 = ReplyKeyboardMarkup(resize_keyboard=True)
    button0 = KeyboardButton(text='Меню')
    keyboard0.add(button0)
    buttonno = KeyboardButton(text='Нет')
    keyboard0.add(buttonno)
    await message.answer('Выбери блюдо или несколько блюд из списка, я посчитаю сумму и пришлю в чат повару', reply_markup=keyboard0)

@dp.message_handler(Text(equals='Меню'))
async def cmd_inline_url(message: Message):
    await message.answer("Заказ:", reply_markup=keyboard)

@dp.callback_query_handler(cb.filter())
async def keyboard_cb_handler(callback: CallbackQuery, callback_data: dict) -> None:
    if callback_data['action'] == :
        await callback.message.answer(str(data))

@dp.message_handler(Text('Фуагра'))
async def fuagra(message):
    await message.answer(text='Что-то еще?', reply_markup=keyboard2)

@dp.message_handler(Text('Конец заказа'))
async def end(message):
    await message.answer('Принято!', reply_markup=ReplyKeyboardRemove())


if __name__ == '__main__':
    executor.start_polling(dp)