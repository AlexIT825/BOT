from telebot import TeleBot, apihelper
import time

file = open("token", "r")
token = file.readline()
token = token.strip()
print(token)

bot = TeleBot(token)

@bot.message_handler(commands=['start', 'begin'])
def start(message):
    print(message)
    bot.send_message(message.from_user.id, "Yes ser, I'm ready to work!"
                                           " First of all, I want to ask you few questions...")
    time.sleep(5.0)
    name = bot.send_message(message.chat.id, "What's your name?")
    bot.register_next_step_handler(name, ask_name)

    time.sleep(13.0)
    msg = bot.send_message(message.chat.id, "How old are you?")
    bot.register_next_step_handler(msg, ask_age)

    time.sleep(6.0)
    bot.send_message(message.from_user.id, "If you want to see sticker, print '/sticker'!")

def ask_name(message):
    text = message.text
    chat_id = message.chat.id
    if text.isdigit():
        name = bot.send_message(chat_id, "It's a string with letters, without numbers and other symbols!")
        bot.register_next_step_handler(name, ask_name)
    else:
        bot.send_message(chat_id, "Hello " + text + ", I'm very glad to see you buddy!")

def ask_age(message):
    text = message.text
    chat_id = message.chat.id
    if not text.isdigit():
        msg = bot.send_message(chat_id, "It's a integer!")
        bot.register_next_step_handler(msg, ask_age)
    else:
        bot.send_message(chat_id, " Thank you! I will remember that your age is " + text)

@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    bot.send_message(message.chat.id, "Take it!:")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAJ8jV65UaRFu8DuFZRUGd9gmLO_FEDjAAKTBwACRvusBAABWx6WplPD3RkE")
    time.sleep(3.0)
    bot.send_message(message.chat.id, "And another one:")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAJ8iV65UYikqU278WOr37VNzOu37wa2AAJdAAMK_MIFZjRMJxxv1nIZBA")

bot.polling(none_stop=True, interval=0)