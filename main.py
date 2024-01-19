import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from instabot import Bot
import time

bot = telebot.TeleBot("6749440736:AAGw3z83kQ2yZEYnjwotgSFVA7SuvQyHS28", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(' فیلم های ایرانی'))


user_dict = {}


class User:
    def __init__(self, name):
        self.name = name

    def set_pasword(self, password):
        self.password = password


@bot.message_handler(commands=['membershib'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Hi there, I am Example bot.
What's your username?
""")
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    chat_id = message.chat.id
    name = message.text
    user = User(name)
    user_dict[chat_id] = user
    msg = bot.reply_to(message, 'How old are you?')

    bot.register_next_step_handler(msg, process_password_step)

def process_password_step(message):
    chat_id = message.chat.id
    password = message.text
    user = user_dict[chat_id]
    user.set_pasword(password)
    ibot = Bot()
    ibot.login(username=user.name, password=user.password)
    print('login shodeh')
    time.sleep(5)
    followers = ibot.get_user_followers(user.name)
    print(f"Followers: {followers}")
    msg = bot.reply_to(message, f"Followers: {followers}")

    # bot.reply_to(message, "Howdy, how are you doing?" , reply_markup=markup)


if __name__ == '__main__':
    bot.infinity_polling()
