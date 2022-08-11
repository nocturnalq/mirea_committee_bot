from cgitb import reset
import telebot
import dotenv
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import os

def load_envs(path: str) -> str:
    dotenv_path = Path(path)
    dotenv.load_dotenv(dotenv_path=dotenv_path)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
SNILS = os.getenv("SNILS")

def parse_table(url):
    snils_list = SNILS.split(',')
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.content, 'html5lib')
    table = soup.find("table", class_="namesTable")
    i = 0
    pos = {}
    for row in table.find_all(attrs={'class':'fio'})[1:]:
        i += 1
        if row.text in snils_list:
            # print(i, row.text)
            pos.update({f"{i}":f"{row.text}"})
    print(pos)
    






def main():
    #  bot = telebot.TeleBot(TELEGRAM_TOKEN)
    parse_table('https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1714961437918539062&prior=any&documentType=original&accepted=1&acceptedEntrant=any&onlyActive=1&onlyPaid=0')



if __name__ == '__main__':
    main()