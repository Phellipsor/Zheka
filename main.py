import schedule
from time import sleep
from threading import Thread
from telebot import TeleBot
from data import week_news, daily_news

bot = TeleBot("6607124610:AAF0rMkhABJvWl5x2Hs7g-_oz8UVzPpCRvk")
users = [353616677, 382267161]

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)
        
def weekly():
    news = "News for next week:\n\n" + f"{'-'*35}\n".join(week_news())
    for us in users:
        bot.send_message(us, news)
    
def daily():
    news_list = daily_news()
    news = "News for today:\n\n" + f"{'-'*35}\n".join(news_list)
    for us in users:
        if len(news_list) > 0:
            bot.send_message(us, news)
        else:
            bot.send_message(us, "No important news for today")
        
if __name__ == "__main__":
    schedule.every().monday.at("08:00", "Europe/Kyiv").do(weekly)
    schedule.every().day.at("08:00", "Europe/Kyiv").do(daily)
    Thread(target=schedule_checker).start()
    
bot.infinity_polling()
