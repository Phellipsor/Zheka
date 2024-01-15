import requests
import json
from datetime import datetime
import calendar

def week_news():
    response = requests.get("https://nfs.faireconomy.media/ff_calendar_thisweek.json?version=4e7b65142501ec6ffc7d6c68048d2fc7")
    data = response.content.decode("utf8").replace("'", '"')
    list_data = json.loads(data)

    formatted_news = []

    for e in list_data:
        if e["impact"] == "High" or e["impact"] == "Medium":
            time = e["date"][11:16]
            date = datetime.strptime(e["date"][0:10], "%Y-%m-%d").date()
            weekday = calendar.day_name[date.weekday()]
            title = e["title"]
            country = e["country"]
            emoji = "🔴"
            text = f"{time} {weekday} {date} \n{country} {emoji} \n{title}\n"
            formatted_news.append(text)

    return formatted_news
    
    
def daily_news():
    response = requests.get("https://nfs.faireconomy.media/ff_calendar_thisweek.json?version=4e7b65142501ec6ffc7d6c68048d2fc7")
    data = response.content.decode("utf8").replace("'", '"')
    list_data = json.loads(data)
    
    formatted_news = []
    
    today = datetime.now().date()
    weekday = calendar.day_name[today.weekday()]
    
    for e in list_data:
        if e["impact"] == "High" or e["impact"] == "Medium":
                if e["date"][0:10] == str(today):
                    time = e["date"][11:16]
                    title = e["title"]
                    country = e["country"]
                    if e["impact"] == "High":
                        emoji = "🔴"
                    else:
                        emoji = "🟠"
                    text = f"{emoji} {country} {time}\n{title}"
                    formatted_news.append(text)
    
    return formatted_news
    
