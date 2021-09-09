import logging

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
import markups as nav

from filters import search

# Dacha API
dacha_url = 'http://192.168.100.128/api/v1/house_list/'
headers = {'content-type': 'application/json'}


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

request_list = {
    "waymark": "",
    "price": "",
    "guest": ""
}

@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, text='Maklersiz hayot guzal hayot',
                           reply_markup=nav.AreaMenu)


@dp.message_handler()
async def bot_message(message: types.Message):

    if 'Hudud' in message.text:
        await bot.send_message(message.from_user.id, 'Hududlar', reply_markup=nav.AreaMenu)
    elif 'Bosh menyu' in message.text:
        await bot.send_message(message.from_user.id, 'Bosh menyu', reply_markup=nav.AreaMenu)
    elif 'Narxi' in message.text:
        await bot.send_message(message.from_user.id, 'Narxi', reply_markup=nav.PriceMenu)
    elif 'Mehmon' in message.text:
        await bot.send_message(message.from_user.id, 'Mehmon', reply_markup=nav.GuestMenu)

    # Hududlar buyicha filtrlash
    if message.text == 'Chorvoq':
        request_list["waymark"] = message.text
        await bot.send_message(message.from_user.id, 'Chorvoqdagi dachalar', reply_markup=nav.PriceMenu)
        logger.debug(nav.AreaMenu)
    elif message.text == 'Xumson':
        request_list["waymark"] = message.text
        await bot.send_message(message.from_user.id, 'Xumson dachalari', reply_markup=nav.PriceMenu)
    elif message.text == 'Yusufxona':
        request_list["waymark"] = message.text
        await bot.send_message(message.from_user.id, 'Yusufxona dachalari', reply_markup=nav.PriceMenu)
    elif message.text == 'Burchmullo':
        request_list["waymark"] = message.text
        await bot.send_message(message.from_user.id, 'Burchmullo dachalari', reply_markup=nav.PriceMenu)
    elif message.text == 'Sijjak':
        request_list["waymark"] = message.text
        await bot.send_message(message.from_user.id, 'Sijjak dachalari', reply_markup=nav.PriceMenu)
    elif message.text == 'Chimyon':
        request_list["waymark"] = message.text
        await bot.send_message(message.from_user.id, 'Chimyon dachalari', reply_markup=nav.PriceMenu)
    elif message.text == 'Barchasi':
        request_list["waymark"] = message.text
        await bot.send_message(message.from_user.id, text='Chorvoq, Xumson, Yusufxona, Burchmullo, Sijjak, Chimyon', parse_mode="html", reply_markup=nav.PriceMenu)




    # Narxi buyicha filtrlash
    if message.text == "0-200":
        request_list["price"] = message.text
        await bot.send_message(message.from_user.id, "0-200 dachalar", reply_markup=nav.GuestMenu)
    elif message.text == '200-400':
        request_list["price"] = message.text
        await bot.send_message(message.from_user.id, '200-400 dachalar', reply_markup=nav.GuestMenu)
    elif message.text == '400-600':
        request_list["price"] = message.text
        await bot.send_message(message.from_user.id, '400-600dachalar', reply_markup=nav.GuestMenu)
    elif message.text == '600+':
        request_list["price"] = message.text
        await bot.send_message(message.from_user.id, '600+ dachalar', reply_markup=nav.GuestMenu)

    # Mehmonlar buyicha filtirlash
    if "Dugonalar" in message.text:
        request_list["guest"] = message.text
        print(request_list)
        house_list = search(request_list)
        print(house_list)
        if house_list:
            i = 0
            while i < len(house_list):
                await bot.send_photo(message.from_user.id, photo=house_list[i], caption=house_list[i+1], parse_mode='html', reply_markup=nav.ReservedMenu)
                i = i + 2
        else:
            await bot.send_message(message.from_user.id, text='Dachalar yuq')
    elif 'Ulfatlar' in message.text:
        request_list["guest"] = message.text
        print(request_list)
        house_list = search(request_list)
        print(house_list)
        if house_list:
            i = 0
            while i < len(house_list):
                await bot.send_photo(message.from_user.id, photo=house_list[i], caption=house_list[i + 1],
                                     parse_mode='html', reply_markup=nav.ReservedMenu)
                i = i + 2
        else:
            await bot.send_message(message.from_user.id, text='Dachalar yuq')
    elif 'Oila bilan' in message.text:
        request_list["guest"] = message.text
        print(request_list)
        house_list = search(request_list)
        print(house_list)
        if house_list:
            i = 0
            while i < len(house_list):
                await bot.send_photo(message.from_user.id, photo=house_list[i], caption=house_list[i + 1],
                                     parse_mode='html', reply_markup=nav.ReservedMenu)
                i = i + 2
        else:
            await bot.send_message(message.from_user.id, text='Dachalar yuq')
    elif 'Qizlar bilan' in message.text:
        request_list["guest"] = message.text
        print(request_list)
        house_list = search(request_list)
        print(house_list)
        if house_list:
            i = 0
            while i < len(house_list):
                await bot.send_photo(message.from_user.id, photo=house_list[i], caption=house_list[i + 1],
                                     parse_mode='html', reply_markup=nav.ReservedMenu)
                i = i + 2
        else:
            await bot.send_message(message.from_user.id, text='Dachalar yuq')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
