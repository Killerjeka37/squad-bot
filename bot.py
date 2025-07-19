
import telebot

TOKEN = "8003269735:AAGLjbAwLKxQwLXsTTjljooNUHcf9vHtaNo"
ADMIN_ID = 5988424240

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Отправь свой ID для ручной проверки.")

@bot.message_handler(func=lambda m: True)
def handle_id(message):
    user_id = message.text.strip()
    bot.send_message(ADMIN_ID, f"Запрос на доступ от ID: {user_id}")
    bot.send_message(message.chat.id, "Спасибо! Ваш ID отправлен на ручную проверку. Ожидайте.")

bot.polling()
