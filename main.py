import schedule
from time import sleep
from threading import Thread
from telebot import TeleBot, types
from data import get_news

bot = TeleBot("6607124610:AAF0rMkhABJvWl5x2Hs7g-_oz8UVzPpCRvk")
zheka = 353616677

@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(msg.chat.id, "Отримаєш звіт на тиждень о 8 ранку понеділка.")

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)
        
def func_to_run():
    news = f"{'-'*35}\n".join(get_news())
    bot.send_message(zheka, news)
        
if __name__ == "__main__":
    schedule.every().monday.at("08:00", "Europe/Kyiv").do(func_to_run)
    Thread(target=schedule_checker).start()

bot.infinity_polling()
