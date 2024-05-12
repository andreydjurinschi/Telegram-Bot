import telebot

from telebot import types

bot = telebot.TeleBot('6365834059:AAEBOcIMANALxWKuXdrY6H2PpRYqkl5J_DY')

def adidas(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Верхняя одежда👕', callback_data='adidas_t_shirt')
    markup.add(btn1)
    btn2 = types.InlineKeyboardButton('Обувь 👟', callback_data='adidas_shoes') # готово
    btn3 = types.InlineKeyboardButton('Нижняя одежда👖', callback_data='adidas_pants') # ujnjjdj
    markup.add(btn3,btn2)
    btn4 = types.InlineKeyboardButton('Назад <-', callback_data='back') #готово
    markup.add(btn4)
    bot.send_message(message.chat.id, 'Какой элемент одежды вас интересует?', reply_markup=markup)
    
def adidas_schoes(message):
    bot.send_message(message.chat.id, 'Присылаем вам рекомендуемые новинки из раздела <b>Adidas Schoes</b>', parse_mode='html')
    photo1 = open('photos/for adidas/shoes1.jpg', 'rb')
    bot.send_photo(message.chat.id, photo1)
    bot.send_message(message.chat.id, '<b>Adidas Samba\n💸120💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 2)

    photo2 = open('photos/for adidas/shoes2.jpg', 'rb')
    bot.send_photo(message.chat.id, photo2)
    bot.send_message(message.chat.id, '<b>Adidas Superstar\n💸210💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 4)

    photo3 = open('photos/for adidas/shoes3.jpg', 'rb')
    bot.send_photo(message.chat.id, photo3)
    bot.send_message(message.chat.id, '<b>Adidas Korn x Campus\n💸170💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 6)

def adidas_t_shirt(message):
    bot.send_message(message.chat.id, 'Присылаем вам рекомендуемые новинки из раздела <b>Adidas Tops & T-Shirts</b>', parse_mode='html')
    photo1 = open('photos/for adidas/korn1.jpg', 'rb')
    bot.send_photo(message.chat.id, photo1)
    bot.send_message(message.chat.id, '<b>adidas X Korn\nDri-FIT T-Shirt\n💸170💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 2)

    photo2 = open('photos/for adidas/fut2.jpg', 'rb')
    bot.send_photo(message.chat.id, photo2)
    bot.send_message(message.chat.id, '<b>Adidas \nCrew Shirt\n💸40💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 4)

    photo3 = open('photos/for adidas/fut3.jpg', 'rb')
    bot.send_photo(message.chat.id, photo3)
    bot.send_message(message.chat.id, '<b>Adidas \nT-Shirt\n💸30💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 6)

def adidas_pants(message):
    bot.send_message(message.chat.id, 'Присылаем вам рекомендуемые новинки из раздела <b>Adidas Pants</b>', parse_mode='html')
    photo1 = open('photos/for adidas/pants1.jpg', 'rb')
    bot.send_photo(message.chat.id, photo1)
    bot.send_message(message.chat.id, '<b>Adidas Balenciaga\nPants\n💸10💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 2)

    photo2 = open('photos/for adidas/pants2.jpg', 'rb')
    bot.send_photo(message.chat.id, photo2)
    bot.send_message(message.chat.id, '<b>Adidas Balenciaga\nJeans\n💸250💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 4)

    photo3 = open('photos/for adidas/pants3.jpg', 'rb')
    bot.send_photo(message.chat.id, photo3)
    bot.send_message(message.chat.id, '<b>Adidas 3-Stripes\nCargo Pants\n💸90💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 6)