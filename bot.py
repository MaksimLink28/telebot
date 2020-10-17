import requests
from bs4 import BeautifulSoup

dollar = "https://www.google.com/search?q=dollar"
user = {"user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

plus = requests.get(dollar, headers = user)
soup = BeautifulSoup(plus.content, "html.parser")

convert = soup.findAll("span",{"class": "DFlfde SwHCTb" ,"data-precision": "2"})

print(convert[0].text)

import telebot

bot = telebot.TeleBot("1379152575:AAHUZf8SU4PdTtPl2dtL1d4czPJXwzpqSYA")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, "Привіт Користувач зараз курс доллара: " + convert[0].text)

if __name__ == '__main__':
     bot.infinity_polling()
