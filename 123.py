from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import (CallbackQuery, KeyboardButton, Message, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.callback_data import CallbackData

API_TOKEN: str = '5783789469:AAEreVKLZID1SPhgg1Ym6Bog4m24OM9767c'
GROUP_ID = '-829598437'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)

cb = CallbackData('keyboard', 'action')

data = {1 : 150, 2: 120, 3: 50, 4: 70, 5: 150, 6: 180, 7: 110, 8: 200, 9: 90, 10: 70}

names = ['Вареная куриная грудка', 'Картофельное пюре', 'Чай зеленый', 'Пюре Агуша (сливки)', 'Суп на курином бульоне', 'Каша овсяная', 'Латте', 'Котлеты на пару', 'Макароны отварные', 'Гречка отварная']
buttons = list()
number = -1
push = 0
sum = 0
check = list()
user_number = 0

for i in range(len(names)):
    button = InlineKeyboardButton(text=names[number+1], callback_data=cb.new(str(push+1)))
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
    buttonno = KeyboardButton(text='Конец заказа')
    keyboard0.add(buttonno)
    await message.answer('Выбери блюдо или несколько блюд из списка, я посчитаю сумму и пришлю в чат повару', reply_markup=keyboard0)

@dp.message_handler(Text(equals='Меню'))
async def cmd_inline_url(message: Message):
    global user_number
    await message.answer("Заказ:", reply_markup=keyboard)
    user_number = message.chat.id

@dp.callback_query_handler(cb.filter())
async def keyboard_cb_handler(callback: CallbackQuery, callback_data: dict):
    with open(str(user_number)+'.txt', 'w', encoding = "utf-8") as file:
        global sum
        global check
        if callback_data['action'] == callback_data['action']:
            dish = names[int(callback_data['action'])-1]
            await callback.message.answer(dish+' - '+str(data[int(callback_data['action'])]))
            await callback.answer()
            check.append(dish)
            sum += data[int(callback_data['action'])]
        string = ', '.join(check)
        file.write(string+'\n')
        file.write(str(sum))

@dp.message_handler(Text(equals='Конец заказа'))
async def end(message: Message):
    global check
    check = []
    with open(str(user_number)+'.txt', 'r', encoding = "utf-8") as f:
        lines = f.readlines()
        data = lines[0]
        count = lines[1]
        global sum
        await message.answer("Принято!\nИтого: "+str(count))
        await bot.send_message(GROUP_ID, data)
        sum = 0

if __name__ == '__main__':
    executor.start_polling(dp)