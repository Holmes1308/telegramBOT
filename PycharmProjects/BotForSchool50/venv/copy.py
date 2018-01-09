def start(message):
    name = message.chat.first_name
    text = "Привет,"
    text2 = ", я бот Школы №50  (http://school50.beluo31.ru) - Ваш помощник по вопросам школы.Ниже вы можете увидеть, что я могу:"
    bot.send_message(message.chat.id, text+name+text2)