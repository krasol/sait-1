import telebot
import sqlite3
import re
bot = telebot.TeleBot('6232398898:AAFnz52qREKyKLTzNs0OWDIUJGbn5SpGZEI');

name = '';
surname = '';
age = "";
nisha = ""

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('1⃣ Начать 1⃣   ')
    bot.send_message(message.from_user.id, 'Привет', reply_markup=user_markup)

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Хай, чтобы начать запись, ответь сначал на несколько моих вопросов, как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id,
                         "Как вас зовут?");
        bot.register_next_step_handler(message, get_name);  # следующий шаг – функция get_name

def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, name + ', расскажите про нишу, в которой вы работаете, а также про товар или услугу, которую хотели бы продвигать');
    bot.register_next_step_handler(message, get_surname );

def get_surname(message): #получаем фамилию
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'Как с вами связаться? если не хотите на этот вопрос отвечать, то поставьте: "-"');
    bot.register_next_step_handler(message, get_age);

def get_nisha(message): #получаем фамилию
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'какой нисшей вы занимаетесь?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global nisha;
    nisha = message.text;
    bot.send_message(message.from_user.id,"Ваша Запись успешно сохранена!")
    s = name+' '+surname+'' + age+ " " + nisha + " " +surname+ " " +str(message.chat.id)

    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    m = []
    m.append(s)
    cursor.execute('INSERT INTO user (users) VALUES(?)', m)
    connect.commit()
    cursor.close()

bot.polling(none_stop=True, interval=0)