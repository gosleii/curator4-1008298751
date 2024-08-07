import telebot

bot = telebot.TeleBot('7218979158:AAEG54DZJCGsjEzTv0dcB-bzol0mJtps5OU')


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, '*Приветствую тебя!*', parse_mode='Markdown')


@bot.message_handler(commands=['croissant'])
def croissant_handler(message):
    bot.send_message(message.chat.id,
                     'Рецепт круассана>>> [Идеальные круассаны](https://eda.ru/recepty/vypechka-deserty/idealnye-kruassany-138570)', parse_mode='Markdown')


@bot.message_handler(commands=['muffin'])
def muffin_handler(message):
    bot.send_message(message.chat.id,
                     'Рецепт маффинов>>> [Шоколадные маффины с кусочками шоколада](https://eda.ru/recepty/vypechka-deserty/shokoladnie-maffini-s-kusochkami-shokolada-36024)', parse_mode='Markdown')


bot.infinity_polling()