import telebot
from main import gen_pas, gen_emoji, flip_coin
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.handler_backends import ContinueHandling
from telebot import types
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("YOUR TOKEN")

bot.delete_my_commands(scope=None, language_code=None)

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("start", "greets you"),
        telebot.types.BotCommand("bye", "says goodbye to you"),
        telebot.types.BotCommand("emodji", "sends you a random emoji"),
        telebot.types.BotCommand("coin", "just flipps a coin and tells you the result"),
        telebot.types.BotCommand("button", "creating a button: (sus)"),
        ])


#bot.message_handler(content_types=["text"])
#def send_hello(message):
#    if message.text == "hello" or "привет":
#        bot.send_message(message.chat.id, f"привет, {message.from_user.first_name}")


@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.send_message(message.chat.id, "Привет! Я твой Telegram бот. Напиши что-нибудь!")


@bot.message_handler(commands=['bye'])
def send_bye(message):
  bot.send_message(message.chat.id, "Пока! Удачи!")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emoji()
    bot.send_message(message.chat.id, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['pasword'])
def password_generation(message):
  password=gen_pas(10)
  bot.reply_to(message, f'Вот твой пароль: {password}')

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, message.text)
  return ContinueHandling()

@bot.message_handler(commands=["button"])
def button_message(message):
   markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
   item1=types.KeyboardButton("Sus")
   markup.add(item1)
   bot.send_message(message.chat.id, "Выберите то что вам нужно", reply_markup=markup)
   

@bot.message_handler(content_types="text")
def message_reply(message):
   if message.text=="Sus":
      bot.send_message(message.chat.id,"https://github.com/sigma434/for-_sigmas")
      

bot.polling()
