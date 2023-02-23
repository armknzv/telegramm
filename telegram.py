import telebot
from extensions import Converter, APIException
from config import *
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands = ['start','help'])
def help(message: telebot.types.Message):
    text = ('Чтобы начать введите команду в формате: \n  <имя валюты, цену которой он хочет узнать> \
<имя валюты, в которой необходимо узнать цену первой валюты> \
 <количество первой валюты.>')
    bot.send_message(message.chat.id  , text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты'
    for key in exchanges.keys():
        text = '\n'.join((text ,key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('Неверное количество параметров')

        answer = Converter.get_price(*values)
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")

    else:
        bot.reply_to(message, answer)


bot.polling(none_stop= True)
