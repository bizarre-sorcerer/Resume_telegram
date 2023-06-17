import telebot
import os

import handle


token = '5967331395:AAHAUexUYWfnRTG5953gPtlaPamh5c4aIbg'
bot = telebot.TeleBot(token)

Resume = {
    'FIO': None,
    'birth_date': None,
    'adres': None,
    'email': None,
    'number': None,
    'experience': None,
    'skills': None,
    'photo': None,
}

counter = [0]


# 
@bot.message_handler(commands=['start', 'help'])
def start(message) -> None:
    bot.send_message(message.chat.id, 'Введите /begin, чтобы создать резюме.')

# 
@bot.message_handler(commands=['begin'])
def create(message) -> None:
    bot.send_message(message.chat.id, 'Введите ФИО')
    print('Бот запущен')
    # 


@bot.message_handler(content_types=['photo', 'text'])
def handle_first_name(message) -> None:
    if counter[0] == 0:
        Resume['FIO'] = message.text

        bot.send_message(message.chat.id, 'Дата рождения')
        counter[0] += 1

    # 
    elif counter[0] == 1:
        Resume['birth_date'] = message.text
        bot.send_message(message.chat.id, 'Адрес')
        counter[0] += 1

# 
    elif counter[0] == 2:
        Resume['adres'] = message.text

        bot.send_message(message.chat.id, 'Email')
        counter[0] += 1

#
    elif counter[0] == 3:
        Resume['email'] = message.text

        bot.send_message(message.chat.id, 'Номер телефона')
        counter[0] += 1

#   
    elif counter[0] == 4:
        Resume['number'] = message.text

        bot.send_message(message.chat.id, 'Опыт работы в сфере')
        counter[0] += 1

# 
    elif counter[0] == 5:
        Resume['experience'] = message.text

        bot.send_message(message.chat.id, 'Навыки/скиллы')
        counter[0] += 1

# 
    elif counter[0] == 6:
        Resume['skills'] = message.text

        bot.send_message(message.chat.id, 'Фото для профиля')

        counter[0] += 1


    elif counter[0] == 7: 
        id =  message.photo[-1].file_id
        file_photo = bot.get_file(id)
        file = bot.download_file(file_photo.file_path)
        
        BASE_PATH = os.path.dirname(__file__)
        MEDIA_URL = os.path.join(BASE_PATH, 'media')
        image_path = f'{MEDIA_URL}/profile.png'


        with open(image_path, 'wb') as img:
            img.write(file)

        Resume['photo'] = image_path

        resume_file = handle.generate_resume_file(Resume)
        bot.send_document(message.chat.id, resume_file)

bot.polling(none_stop=True)
