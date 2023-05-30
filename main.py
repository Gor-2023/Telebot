import telebot
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot('5646615694:AAFhNNWtqSpP4saMQOg13J_XfDOEi06R1E4')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! Please write the programming language you want to work with.')

@bot.message_handler(func=lambda message: True)
def info(message):
    programming_language = message.text.lower()
    if programming_language:
        data = []
        for p in range(1, 5):

            url =f'https://staff.am/am/jobs?JobsFilter%5Bcompany%5D=&JobsFilter%5Bkey_word%5D={programming_language}&JobsFilter%5Bjob_candidate_level%5D=&JobsFilter%5Bcategory%5D=&JobsFilter%5Bcategory%5D%5B%5D=1&JobsFilter%5Bjob_type%5D=&JobsFilter%5Bsalary%5D=&JobsFilter%5Bjob_term%5D=&JobsFilter%5Bjob_city%5D=&JobsFilter%5Bsort_by%5D=0&&JobsFilter%5Bsort_by%5D=0'


            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            article = soup.find("div", class_="list-view").find_all("div", class_="web_item_card hs_job_list_item")
            data = []
            for i in article:
                link = "https://staff.am" + i.find("a", class_="history_block_style history_block_padding").get('href')
                data.append([link])


        for link in data:
            bot.send_message(message.chat.id, link)

bot.polling(none_stop=True)



