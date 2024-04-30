import requests  # позволяет отправлять запросы
from bs4 import BeautifulSoup as BS
import csv

HOST= 'https://www.banki.ru/'
URL='https://www.banki.ru/products/creditcards/'
HEADERS = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup=BS(html, 'html.parser')
    items=soup.find_all('div', class_='bg-minor-black-lighten2')
    massive=[]
    print(items)


html=get_html(URL)
print(html)
get_content(html.text)
