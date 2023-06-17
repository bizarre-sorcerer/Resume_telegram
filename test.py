import telebot
import os

token = '5967331395:AAHAUexUYWfnRTG5953gPtlaPamh5c4aIbg'
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def asdf(message):
    bot.send_message(message.chat.id, 'Photo')

@bot.message_handler(content_types=['photo'])
def photo(message):
    id =  message.photo[-1].file_id
    file_photo = bot.get_file(id)
    file = bot.download_file(file_photo.file_path)

    BASE_PATH = os.path.dirname(__file__)
    MEDIA_URL = os.path.join(BASE_PATH, 'media')

    with open(f'{MEDIA_URL}/profile.png', 'wb') as img:
        img.write(file)

    bot.send_photo(message.chat.id, photo=open(f'{MEDIA_URL}/profile.png', 'rb'))

bot.polling(none_stop=True)