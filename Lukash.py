import telebot
import codecs
import random
from telebot import types

TOKEN = '5047656036:AAFl0g8s11lgQAx1EHIlZVgDD45KG0Lgpg0'
bot = telebot.TeleBot(TOKEN)

# Зчитуємо тхт файл та записуємо в ліст
notmyjokes = list()
file = codecs.open("Jokes_by_arthor.txt", "r", "utf-8")
for line in file.readlines():
    notmyjokes.append(line.strip())
file.close()

# Функция, обрабатывающая команду /start
@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Доброго дня, Пане! ')

# створюємо кнопку, яка буде виводити напис самої кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Автор...")
    item2 = types.KeyboardButton("Фото творця...")
    item3 = types.KeyboardButton("Вікторина...")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id,'Чого бажаєте? ', reply_markup = markup)

# Після натискання кнопки кидається посилання
@bot.message_handler(content_types = ["text"])
def message_reply(message):
    if message.text == "Автор...":
        bot.send_message(message.chat.id, 'https://bipbap.ru/wp-content/uploads/2017/04/edc9a7a07b86.jpg')
    if message.text == "Фото творця...":
        bot.send_message(message.chat.id, 'vstavutb karinky')
    if message.text == "Вікторина...":
        bot.send_message(message.chat.id, random.choice(notmyjokes))

#final station

# Запускаем бота
bot.infinity_polling()