import telebot

from telebot import types

bot = telebot.TeleBot('6365834059:AAEBOcIMANALxWKuXdrY6H2PpRYqkl5J_DY')

def nike(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Верхняя одежда👕', callback_data='nike_t_shirt')
    markup.add(btn1)
    btn2 = types.InlineKeyboardButton('Обувь 👟', callback_data='nike_shoes') # готово
    btn3 = types.InlineKeyboardButton('Нижняя одежда👖', callback_data='nike_pants')
    markup.add(btn3,btn2)
    btn4 = types.InlineKeyboardButton('Назад <-', callback_data='back') #готово
    markup.add(btn4)
    bot.send_message(message.chat.id, 'Какой элемент одежды вас интересует?', reply_markup=markup)

def nike_schoes(message):
    bot.send_message(message.chat.id, 'Присылаем вам рекомендуемые новинки из раздела <b>Nike Schoes</b>', parse_mode='html')
    photo1 = open('photos/for nike/dunk-low-retro-mens-shoes-5FQWGR.png', 'rb')
    bot.send_photo(message.chat.id, photo1)
    bot.send_message(message.chat.id, '<b>Nike dunk low retro\n💸120💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 2)

    photo2 = open('photos/for nike/air-vapormax-plus-mens-shoes-nC0dzF.png', 'rb')
    bot.send_photo(message.chat.id, photo2)
    bot.send_message(message.chat.id, '<b>Nike air vapormax plus\n💸210💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 4)

    photo3 = open('photos/for nike/air-max-koko-womens-sandals-gwRZGk.png', 'rb')
    bot.send_photo(message.chat.id, photo3)
    bot.send_message(message.chat.id, '<b>Nike max koko\n💸100💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 6)

def nike_t_shirt(message):
    bot.send_message(message.chat.id, 'Присылаем вам рекомендуемые новинки из раздела <b>Nike Tops & T-Shirts</b>', parse_mode='html')
    photo1 = open('photos/for nike/tshirt1.png', 'rb')
    bot.send_photo(message.chat.id, photo1)
    bot.send_message(message.chat.id, '<b>Nike ACG\nDri-FIT T-Shirt\n💸55💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 2)

    photo2 = open('photos/for nike/rubaska.jpg', 'rb')
    bot.send_photo(message.chat.id, photo2)
    bot.send_message(message.chat.id, '<b>Nike Life\nLong-Sleeve Oxford Button-Down Shirt\n💸100💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 4)

    photo3 = open('photos/for nike/jens.png', 'rb')
    bot.send_photo(message.chat.id, photo3)
    bot.send_message(message.chat.id, '<b>Nike Pro\nLong-Sleeve Top\n💸100💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 6)

def nike_pants(message):
    bot.send_message(message.chat.id, 'Присылаем вам рекомендуемые новинки из раздела <b>Nike Pants</b>', parse_mode='html')
    photo1 = open('photos/for nike/pants1.png', 'rb')
    bot.send_photo(message.chat.id, photo1)
    bot.send_message(message.chat.id, '<b>Nike Club\nCargo Pants\n💸95💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 2)

    photo2 = open('photos/for nike/pats2.jpg', 'rb')
    bot.send_photo(message.chat.id, photo2)
    bot.send_message(message.chat.id, '<b>Nike Life\nCarpenter Pants\n💸120💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 4)

    photo3 = open('photos/for nike/jenss.png', 'rb')
    bot.send_photo(message.chat.id, photo3)
    bot.send_message(message.chat.id, '<b>Nike Sportswear\nPants\n💸100💸</b>',parse_mode='html', reply_to_message_id=message.message_id + 6)