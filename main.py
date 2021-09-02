import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
import random
import markups as nav

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}'.format(message.from_user), reply_markup = nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Рандомное число':
        await bot.send_message(message.from_user.id, 'Ваше число: ' + str(random.randint(100, 9999)))
    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup = nav.mainMenu)
    elif message.text == 'Другое':
        await bot.send_message(message.from_user.id, 'текст', reply_markup = nav.otherMenu)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)