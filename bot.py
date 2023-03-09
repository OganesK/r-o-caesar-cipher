import telebot
from telebot import types

from caesarChipher import encrypt, decrypt

bot = telebot.TeleBot('6031489118:AAHLOcWYJ4fcfN5vjb-VTThlMYsf2v2oGnE')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔐 Зашифровать")
    btn2 = types.KeyboardButton("🔒 Расшифровать")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "👋 Привет! Я бот, который может шифровать и дешифровать текст шифром Цезаря!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '🔐 Зашифровать':
        bot.send_message(message.from_user.id, '💬 Отправьте мне текст, который необходимо зашифровать. Отправьте мне "Зашифруй мне: <ваш текст> | <укажите числом необходимое смещение>"')
    elif message.text == '🔒 Расшифровать':
        bot.send_message(message.from_user.id, '💬 Отправьте мне текст, который необходимо расшифровать. Отправьте мне "Расшифруй мне: <ваш текст> | <укажите числом необходимое смещение>"')
    elif 'Зашифруй мне' in message.text:
        splittedMessage = message.text.split(':')[1].split('|')
        text = splittedMessage[0].strip()
        offset = splittedMessage[1]
        encryptedMessage = encrypt(text, int(offset))
        bot.send_message(message.from_user.id, 'Вот ваше расшифрованное сообщение: {0}'.format(encryptedMessage))
    elif 'Расшифруй мне' in message.text:
        splittedMessage = message.text.split(':')[1].split('|')
        text = splittedMessage[0].strip()
        offset = splittedMessage[1]
        decryptedMessage = decrypt(text, int(offset))
        bot.send_message(message.from_user.id, 'Вот ваше расшифрованное сообщение: {0}'.format(decryptedMessage))
    else:
        bot.send_message(message.from_user.id, '🤔 Не понял вашего сообщения. Для того чтобы я мог зашифровать/расшифоровать текст следуйте пожалуйста инструкциям')
        
bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
