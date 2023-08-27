import os
import requests
import telebot

BOT_TOKEN ='6273719064:AAFQOHlvf9G0dyImyQJXTDB-3a83GGqkhYM'
bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "How you doing?")


@bot.message_handler(func=lambda message: True)
def sign_handler(message):
    text = "Enter the transaction:"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, handle_message)

def handle_message(message):
    chat_id = message.chat.id
    form_data = message.text  
    js = {"text": form_data}

    external_api_url = 'http://127.0.0.1:8000/entry'
    response = requests.post(external_api_url, data=js)
    status_code = response.status_code
    response = response.json()
    output_message = f'*Transaction:* {response["log"]}\n*Category:* {response["tag"]}\n*Amount:* {response["amount"]}'
    if status_code == 200:
        bot.send_message(chat_id, output_message)
    else:
        bot.send_message(chat_id, "Failed to send form data to the API.")



bot.infinity_polling()