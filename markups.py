from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji

btnMain = KeyboardButton('Bosh menyu')
btnArea = KeyboardButton('Hududlar')

# --- Reserved Menu ---
ReservedMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(btnMain)


# --- Main Menu ---
btnArea = KeyboardButton(emoji.emojize(':sunrise:') + ' Hudud')
btnReservStatus = KeyboardButton(emoji.emojize(':balance_scale:') + ' Holati')
btnPrice = KeyboardButton(emoji.emojize(':money_bag:') +' Narxi')
btnGuest = KeyboardButton(emoji.emojize(':restroom:') + ' Mehmon')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnArea, btnReservStatus).row(btnPrice, btnGuest)



# --- Hudud Menu ---
btnChorvoq = KeyboardButton('Chorvoq')
btnXumson = KeyboardButton('Xumson')
btnYusufxona = KeyboardButton('Yusufxona')
btnBurchmullo = KeyboardButton('Burchmullo')
btnSijjak = KeyboardButton('Sijjak')
btnChimyon = KeyboardButton('Chimyon')
btnAllArea = KeyboardButton('Barchasi')
AreaMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(btnChorvoq, btnXumson).row(btnYusufxona, btnBurchmullo).row(btnSijjak, btnChimyon).row(btnAllArea)

# --- Narxi Menu ---
btnPrice200 = KeyboardButton("0-200")
btnPrice400 = KeyboardButton("200-400")
btnPrice600 = KeyboardButton("400-600")
btnPriceMax = KeyboardButton("600+")
PriceMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(btnPrice200, btnPrice400).row(btnPrice600, btnPriceMax).row(btnMain)


# --- Mehmonlar Menu ---
btnOnlyWomans = KeyboardButton("Dugonalar")
btnOnlyMens = KeyboardButton("Ulfatlar")
btnOnlyFamily = KeyboardButton("Oila bilan")
btnAllPeople = KeyboardButton("Qizlar bilan")
GuestMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(btnOnlyMens, btnOnlyWomans, ).row(btnOnlyFamily, btnAllPeople).row(btnMain)

