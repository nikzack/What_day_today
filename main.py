import telebot
import requests
from bs4 import BeautifulSoup as BS
import time
import schedule

def get_names():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
    url = "https://www.calend.ru/"
    r = requests.get(url, headers=headers)
    soup = BS(r.text, "html.parser")

    table = soup.find('ul', {'class': 'itemsNet'})
    spans = table.find_all('span', {'class': 'title'})
    names = []
    for span in spans:
        name = span.find('a').text
        names.append(name)
    return names

def sand(chat_id):
    answer = ""
    names = get_names()
    for name in names:
        answer = answer+name+"\n"
    bot.send_message(chat_id, "Праздники:\n" + answer)

chat_id = 856774248
token = '1123880191:AAFeXitxFGL_ViTBpusV1ogjqnTJeO4qgKk'

bot = telebot.TeleBot(token)

schedule.every().day.at("10:00").do(sand, chat_id = chat_id)
#schedule.every(10).seconds.do(sand, chat_id = chat_id)
while True:
    schedule.run_pending()
    time.sleep(1)