import telebot
import constants
import time
bot = telebot.TeleBot(constants.token)
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('Хочу узнать расположение', 'Хочу узнать расписание')
    name = message.chat.first_name
    text = "Привет,"
    text2 = ", я бот Школы №50  (http://school50.beluo31.ru) - Ваш помощник по вопросам школы.Ниже вы можете увидеть, что я могу:"
    bot.send_message(message.from_user.id,text+name+text2,reply_markup=user_markup)
    hide_markup = telebot.types.ReplyKeyboardHide
    bot.send_message(message.from_user.id,'..', reply_markup=hide_markup)
def handle_text(message):
    if message.text == ''
bot.polling(none_stop=True)