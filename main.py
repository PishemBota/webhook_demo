import telebot
from flask import Flask, request #этим заменяем импорт фласка

TOKEN = "<токен>"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

bot.set_webhook(url="https://<название>.ngrok.io/<токен>")#добавляем до всех функций

@app.route('/')
def index():
	return '<h1>Webhook work - OK<h1>'

@bot.message_handler(commands=['start'])
def start(m):
	bot.send_message(m.chat.id, 'Привет, человек!')
	
@app.route("/<токен>", methods=['POST']) #отд. функция
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(
        request.stream.read().decode("utf-8"))])

    return "ok", 200

app.run()