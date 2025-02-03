import telebot
import random
from flask import Flask, request

# Токен бота
TOKEN = "8004173733:AAFqTNogPXoYiEv50lopxwklHDxjFM8vdrw"
bot = telebot.TeleBot(TOKEN)

# Flask приложение
app = Flask(__name__)

# Логирование сообщений
def log_message(message):
    with open('log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write(f"{message.from_user.username}: {message.text}\n")

# Обработка всех сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    log_message(message)

    # Условия для ответов
    if message.text.lower() == 'дед':
        bot.reply_to(message, 'Нахуй одет')
        return

    if message.from_user.username in ['tonynow300689', 'FenevAPP']:
        if random.randint(1, 10) == 1:  # 10% шанс
            bot.reply_to(message, 'Шутник хуев')
            return

    if message.from_user.username == 'boian29':
        if random.randint(1, 20) == 1:  # 5% шанс
            bot.reply_to(message, 'Ну ты и хуйло')
            return

    if random.randint(1, 20) == 1:  # 5% шанс для любого сообщения
        bot.reply_to(message, 'Ну и хуйню ты несёшь')

# Вебхук
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'ok', 200

# Точка входа
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
