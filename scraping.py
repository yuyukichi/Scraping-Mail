import requests
from bs4 import BeautifulSoup
import re


def scraping():
    url = 'https://www.hogehoge.co.jp/company/news/'
    # 取得したいURL

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    elems = soup.find_all('a', class_='c-news__link')
    #                    　⬆ここと⬆で要素とクラスを指定
    return str(elems[0].contents[0])+str(elems[0].attrs["href"])
