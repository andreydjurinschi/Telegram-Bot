import telebot
import re
from telebot import types
from  nike import nike, nike_schoes, nike_t_shirt, nike_pants
from adidas import  adidas, adidas_schoes, adidas_t_shirt, adidas_pants
from asics import asics, asics_schoes, asics_t_shirt, asics_pants
import time

bot = telebot.TeleBot('6365834059:AAEBOcIMANALxWKuXdrY6H2PpRYqkl5J_DY')
@bot.message_handler(commands=['start', 'begin'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Готов')
    btn2 = types.KeyboardButton('Не готов')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, f'Здравствуй {message.from_user.first_name} {message.from_user.last_name}. Добро пожаловать в чат-бот <b>WebAppBot</b>. Теперь тебе нужно провести небольшую регистрацию! \nНапишите или нажмите <b>"готов"</b>, если вы готовы и <b>"не готов"</b>, если вы не готовы😇', parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, on_click_process_response)
def on_click_process_response(message):
    if message.text.lower() == 'готов':
        remove = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Как мне к вам обращаться?', reply_markup=remove)
        bot.register_next_step_handler(message, process_name)
    elif message.text.lower() == 'не готов':
        remove = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,f'{message.from_user.username} отказались от услуг нашего бота, тогда немного отдохните!',reply_markup=remove)
    else:
        handle_invalid_input(message)

def handle_invalid_input(message):
    bot.send_message(message.chat.id, 'Я не понимаю ваш ввод...')
    markup = types.ReplyKeyboardMarkup()
    btn = types.KeyboardButton('Продолжить')
    markup.add(btn)
    bot.send_message(message.chat.id, 'Пожалуйста, введите "готов" или "не готов"', reply_markup=markup)
    bot.register_next_step_handler(message, start)

def process_name(message):
    name = message.text
    bot.reply_to(message, f'{name}, теперь мне нужен ваш номер(+373ХХХХХХХХХ)🇲🇩:')
    bot.register_next_step_handler(message, process_number)


def process_number(message):
    try:
        template = r'^\+373\d{8}$'
        number = message.text
        if re.match(template, number):
            bot.reply_to(message, f'Ваша регистрация прошла успешно, можете начинать шоппинг🛍!')
    #       bot.send_sticker(message.chat.id, 'CAACAgEAAxkBAAEFSb9mO7vEaMPQAAFLAgdOH9n3pGXjvgEAAjsGAAJoY4MMUZbo5YMphZY1BA')
            bot.send_message(message.chat.id, '/shop')
        else:
            raise ValueError("Не соответствует шаблону")
    except ValueError:
        bot.reply_to(message, 'К сожалению, ваш номер не соответствует шаблону 🇲🇩 +373XXXXXXXX. Пожалуйста, введите номер еще раз:')
        bot.register_next_step_handler(message, process_number)

@bot.message_handler(commands=['shop'])
def step_after_registration(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Да')
    btn2 = types.KeyboardButton('Нет')
    markup.row(btn1,btn2)
    bot.send_message(message.chat.id, 'Вы прошли регистрацию?', reply_markup=markup)
    bot.register_next_step_handler(message, registration_verification)

def registration_verification(message):
    if message.text.lower() == 'да':
        remove = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Прекрасно, давайте начнем закупаться!', reply_markup=remove)
        main_shop_menu(message)
    elif message.text.lower() == 'нет':
        remove = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Вы обязательно должны пройти регистрацию, нажмите на следующее сообщениe:', reply_markup=remove)
        bot.send_message(message.chat.id, '/start')
    else:
        bot.send_message(message.chat.id, 'Не понял')




def main_shop_menu(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Nike ✅', callback_data='nike_next_step')
    markup.add(btn1)
    btn2 = types.InlineKeyboardButton('Adidas ✅', callback_data='adidas_next_step')
    btn3 = types.InlineKeyboardButton('Puma ❌', callback_data='puma_next_step')
    markup.add(btn2,btn3)
    btn4 = types.InlineKeyboardButton('Asics ✅', callback_data='asics_next_step')
    btn5 = types.InlineKeyboardButton('Joma ❌', callback_data='joma_next_step')
    markup.add(btn5, btn4)
    bot.send_message(message.chat.id, 'Какой бренд одежды вас интересует?\n\n✅ - есть возможность для заказа \n❌ - нет возможности для заказа', reply_markup=markup)



@bot.callback_query_handler(func=lambda call:True)
def call_brand(call):
    if call.message:
# Кнопка назад и все кнопки для Nike
        if call.data == 'nike_next_step':
            photo = open('photos/for nike/nike.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, '<b>На данный момент одежда фирмы Nike доступна для заказа!</b> Кидаем вам ссылку, как только найдете подходящий элемент'
                                                   ' одежды пришлите нам ссылку продукта обратно в чат!', parse_mode='html')
            nike(call.message)
        elif call.data == 'back':
            main_shop_menu(call.message)
        elif call.data == 'nike_shoes':
            nike_schoes(call.message)
            markup_schoes = types.InlineKeyboardMarkup()
            btn_schoes = types.InlineKeyboardButton('Перейти за покупкой', url='https://www.nike.com/w/mens-shoes-nik1zy7ok')
            btn_back = types.InlineKeyboardButton('Назад', callback_data='back')
            markup_schoes.add(btn_schoes, btn_back)
            bot.send_message(call.message.chat.id, "По ссылке ниже вам будут доступны и другие модели обуви\n❗не забывайте перекинуть текст ссылки обратно в чат ", reply_markup=markup_schoes)
        elif call.data == 'nike_t_shirt':
            nike_t_shirt(call.message)
            markup_shirt = types.InlineKeyboardMarkup()
            btn_tshirt = types.InlineKeyboardButton('Перейти за покупкой', url='https://www.nike.com/w/mens-tops-t-shirts-9om13znik1')
            btn_back = types.InlineKeyboardButton('Назад', callback_data='back')
            markup_shirt.add(btn_tshirt, btn_back)
            bot.send_message(call.message.chat.id, "По ссылке ниже вам будут доступны и другие модели верхней одежды\n❗не забывайте перекинуть текст ссылки обратно в чат ", reply_markup=markup_shirt)
        elif call.data == 'nike_pants':
            nike_pants(call.message)
            markup_pants = types.InlineKeyboardMarkup()
            btn_pants = types.InlineKeyboardButton('Перейти за покупкой', url='https://www.nike.com/w/mens-pants-tights-2kq19znik1')
            btn_back = types.InlineKeyboardButton('Назад', callback_data='back')
            markup_pants.add(btn_pants, btn_back)
            bot.send_message(call.message.chat.id, "По ссылке ниже вам будут доступны и другие модели нижней одежды\n❗не забывайте перекинуть текст ссылки обратно в чат ", reply_markup=markup_pants)

#Кнопка назад и все кнопки для Adidas

        elif call.data == 'adidas_next_step':
            photo = open('photos/for adidas/adidas_logo.png', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id,
                            '<b>Прекрасно, Adidas доступна для заказа!</b> Кидаем вам ссылку, как только найдете подходящий элемент'
                             ' одежды пришлите нам ссылку на него обратно в чат!', parse_mode='html')
            adidas(call.message)

        elif call.data == 'adidas_shoes':
            adidas_schoes(call.message)
            markup_schoes = types.InlineKeyboardMarkup()
            btn_schoes = types.InlineKeyboardButton('Перейти за покупкой',url='https://www.adidas.com/us/men-shoes')
            btn_back = types.InlineKeyboardButton('Назад', callback_data='back')
            markup_schoes.add(btn_schoes, btn_back)
            bot.send_message(call.message.chat.id,
                             "По ссылке ниже вам будут доступны и другие модели обуви\n❗️не забывайте перекинуть текст ссылки обратно в чат ",
                             reply_markup=markup_schoes)
        elif call.data == 'adidas_t_shirt':
            adidas_t_shirt(call.message)
            markup_shirt = types.InlineKeyboardMarkup()
            btn_tshirt = types.InlineKeyboardButton('Перейти за покупкой',url='https://www.adidas.com/us/men-tops')
            btn_back = types.InlineKeyboardButton('Назад', callback_data='back')
            markup_shirt.add(btn_tshirt, btn_back)

            bot.send_message(call.message.chat.id,
                             "По ссылке ниже вам будут доступны и другие модели верхней одежды\n❗не забывайте перекинуть текст ссылки обратно в чат",
                             reply_markup=markup_shirt)
        elif call.data == 'adidas_pants':
            adidas_pants(call.message)
            markup_pants = types.InlineKeyboardMarkup()
            btn_pants = types.InlineKeyboardButton('Перейти за покупкой',
                                                    url='https://www.adidas.com/us/men-pants')
            btn_back = types.InlineKeyboardButton('Назад', callback_data='back')
            markup_pants.add(btn_pants, btn_back)
            bot.send_message(call.message.chat.id,
                             "По ссылке ниже вам будут доступны и другие модели нижней одежды\n❗️ не забывайте перекинуть текст ссылки обратно в чат ",
                             reply_markup=markup_pants)

#Кнопка назад и все кнопки для Asics

        elif call.data == 'asics_next_step':
            photo = open('photos/for asics/asics_logo.png', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id,
                            '<b>Прекрасно, Asics есть в наличии!</b> Кидаем вам ссылку, как только найдете подходящий элемент'
                             ' одежды пришлите нам ссылку на него обратно в чат!', parse_mode='html')
            asics(call.message)

        elif call.data == 'asics_shoes':
            asics_schoes(call.message)
            markup_schoes = types.InlineKeyboardMarkup()
            btn_schoes = types.InlineKeyboardButton('Перейти за покупкой',
                                                    url='https://www.asics.com/nl/en-nl/mens-shoes/c/as10200000/')
            btn_back = types.InlineKeyboardButton('Назад', callback_data='back')
            markup_schoes.add(btn_schoes, btn_back)
            bot.send_message(call.message.chat.id,
                             "По ссылке ниже вам будут доступны и другие модели обуви\n❗️не забывайте перекинуть текст ссылки обратно в чат ",
                             reply_markup=markup_schoes)
        elif call.data == 'asics_t_shirt':
            asics_t_shirt(call.message)
            markup_shirt = types.InlineKeyboardMarkup()
            btn_tshirt = types.InlineKeyboardButton('Перейти за покупкой',
                                                    url='https://www.asics.com/nl/en-nl/men-tops/c/as10301000/')
            btn_back = types.InlineKeyboardButton('Назад', callback_data='back')
            markup_shirt.add(btn_tshirt, btn_back)
            bot.send_message(call.message.chat.id,
                             "По ссылке ниже вам будут доступны и другие модели верхней одежды\n❗не забывайте перекинуть текст ссылки обратно в чат",
                             reply_markup=markup_shirt)
        elif call.data == 'asics_pants':
            asics_pants(call.message)
            markup_pants = types.InlineKeyboardMarkup()
            btn_pants = types.InlineKeyboardButton('Перейти за покупкой',
                                                    url='https://www.asics.com/nl/en-nl/men-bottoms/c/as10302000/')
            btn_back = types.InlineKeyboardButton('Назад', callback_data='back')
            markup_pants.add(btn_pants, btn_back)
            bot.send_message(call.message.chat.id,
                             "По ссылке ниже вам будут доступны и другие модели нижней одежды\n❗️ не забывайте перекинуть текст ссылки обратно в чат ",
                             reply_markup=markup_pants)
# Отсутствующие бренды
        elif call.data == 'puma_next_step':
            photo = open('photos/for puma/puma-logo-cover-958x575.png', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            markup_back = types.InlineKeyboardMarkup()
            btn_back = types.InlineKeyboardButton('Вернуться к брендам', callback_data='back')
            markup_back.add(btn_back)
            bot.send_message(call.message.chat.id, 'На данный момент мы не можем брать заказы от бренда Puma, выбери бренд, атрибутику которого мы можем заказать или же вам придется немного подождать', reply_markup=markup_back)

        elif call.data == 'joma_next_step':
            photo = open('photos/for joma/joma5328.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            markup_back = types.InlineKeyboardMarkup()
            btn_back = types.InlineKeyboardButton('Вернуться к брендам', callback_data='back')
            markup_back.add(btn_back)
            bot.send_message(call.message.chat.id, 'На данный момент мы не можем брать заказы от бренда Joma, выбери бренд, атрибутику которого мы можем заказать или же вам придется немного подождать', reply_markup=markup_back)
        elif call.data == 'info_next_step':
            markup2 = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('Пройти опрос', callback_data='query')
            btn2 = types.InlineKeyboardButton('Назад', callback_data='refuse')
            markup2.add(btn1, btn2)
            bot.send_message(call.message.chat.id, '<b>❗️НЕ ЗАБЫВАЕМ❗️</b> \n\n Перед каждым запросом, мы должны провести небольшой опрос по поводу вашего подходящего бренда', reply_markup=markup2, parse_mode='html')
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEFSfRmO8UUKPcp0Y0Ek9iEMsAaBlcBQgAC6w4AAqwaWUh7Bdoy6pPI_TUE')
        elif call.data == 'query':
            bot.send_message(call.message.chat.id, '❗️Нажмите на мое следующее сообщение, мы вас перекинем на сайт с оценкой самочувтсвия❗️')
            disposition(call.message)
        elif call.data == 'refuse':
            bot.send_message(call.message.chat.id, 'Нет, нам важно знать ваше настроение!')
            disposition(call.message)


@bot.message_handler(commands=['info'])
def info(message):
    photo = open('photos/for nike/WAI.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Далее', callback_data='info_next_step'))
    bot.send_message(message.chat.id, '<b>"WHALE AI"</b> - это интеллектуальный чат-бот для Telegram, созданный на основе '
                                      'передовой технологии искусственного интеллекта. С "WHALE AI" пользователи '
                                      'могут получить ответы на свои вопросы, общаться на различные темы, '
                                      'получать рекомендации и даже проводить небольшие обучающие сессии.\n\nНаш бот '
                                      'обладает широким спектром знаний и способен адаптироваться к вашим '
                                      'потребностям, предоставляя информацию по запросу. Он также может помочь вам '
                                      'развивать навыки и знания в различных областях благодаря своей способности '
                                      'генерировать интересные и информативные ответы.\n\n<b>"WHALE AI"</b> - это ваш '
                                      'надежный помощник в мире знаний и общения, всегда готовый предложить вам '
                                      'помощь и поддержку в любое время.', reply_markup=markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.entities is not None and any(entity.type == 'url' for entity in message.entities))
def links(message):
    bot.send_message(message.chat.id, 'Прекрасно, мы отправим данную ссылку <b>отделу приема заказов</b> и они вам перезвонят!\nУ вас есть время для поиска других элементов одежды', parse_mode='html')
@bot.message_handler(commands=['disposition'])
def disposition(message):
    markup3 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти по ссылке', url='https://www.marieclaire.ru/moda/test-kakoi-modnyi-brend-vam-podkhodit/')
    markup3.add(btn1)
    bot.send_message(message.chat.id, 'Тест на подходящий бренд одежды', reply_markup=markup3)
    bot.send_message(message.chat.id, 'Мы надеемся, что ваш бренд доступен для заказов, пришлите нам "/start" ')

@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.reply_to(message, 'К сожалению, я еще не научился обрабатывать фотографии🥲')

bot.polling(non_stop=True)