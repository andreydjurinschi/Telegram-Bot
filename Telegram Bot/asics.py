import telebot

from telebot import types

bot = telebot.TeleBot('6365834059:AAEBOcIMANALxWKuXdrY6H2PpRYqkl5J_DY')

def asics(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Верхняя одежда👕', callback_data='asics_t_shirt')
    markup.add(btn1)
    btn2 = types.InlineKeyboardButton('Обувь 👟', callback_data='asics_shoes') # готово
    btn3 = types.InlineKeyboardButton('Нижняя одежда👖', callback_data='asics_pants') # ujnjjdj
    markup.add(btn3,btn2)
    btn4 = types.InlineKeyboardButton('Назад <-', callback_data='back') #готово
    markup.add(btn4)
    bot.send_message(message.chat.id, 'Какой элемент одежды вас интересует?', reply_markup=markup)
    
def asics_schoes(message):
    bot.send_message(message.chat.id, 'Присылаем вам рекомендуемые новинки из раздела <b>Asics Schoes</b>', parse_mode='html')
    photo1 = open('photos/for asics/schoes1.jpg', 'rb')
    bot.send_photo(message.chat.id, photo1)
    bot.send_message(message.chat.id, '<b>Asics GEL\n💸120💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 2)

    photo2 = open('photos/for asics/shoes2.jpg', 'rb')
    bot.send_photo(message.chat.id, photo2)
    bot.send_message(message.chat.id, '<b>Asics GEL-QUANTUM\n💸210💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 4)

    photo3 = open('photos/for asics/shoes3.jpg', 'rb')
    bot.send_photo(message.chat.id, photo3)
    bot.send_message(message.chat.id, '<b>Asics GEL-3\n💸170💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 6)

def asics_t_shirt(message):
    bot.send_message(message.chat.id, 'Присылаем вам рекомендуемые новинки из раздела <b>Asics Tops & T-Shirts</b>', parse_mode='html')
    photo1 = open('photos/for asics/shirt1.jpg', 'rb')
    bot.send_photo(message.chat.id, photo1)
    bot.send_message(message.chat.id, '<b>Asiscs\nT-Shirt\n💸80💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 2)

    photo2 = open('photos/for asics/shirt2.jpg', 'rb')
    bot.send_photo(message.chat.id, photo2)
    bot.send_message(message.chat.id, '<b>Asics\nTennis Shirt\n💸150💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 4)

    photo3 = open('photos/for asics/shirt3.jpg', 'rb')
    bot.send_photo(message.chat.id, photo3)
    bot.send_message(message.chat.id, '<b>Asics \nT-Shirt\n💸15💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 6)

def asics_pants(message):
    bot.send_message(message.chat.id, 'Присылаем вам рекомендуемые новинки из раздела <b>Asics Pants</b>', parse_mode='html')
    photo1 = open('photos/for asics/pants1.jpg', 'rb')
    bot.send_photo(message.chat.id, photo1)
    bot.send_message(message.chat.id, '<b>Asics STRETCH\nPants\n💸30💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 2)

    photo2 = open('photos/for asics/pants2.jpg', 'rb')
    bot.send_photo(message.chat.id, photo2)
    bot.send_message(message.chat.id, '<b>Asics FT pant\nSport pants\n💸250💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 4)

    photo3 = open('photos/for asics/pants3.jpg', 'rb')
    bot.send_photo(message.chat.id, photo3)
    bot.send_message(message.chat.id, '<b>Asics Race\nPants\n💸90💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 6)