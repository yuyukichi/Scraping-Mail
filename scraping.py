import requests
from bs4 import BeautifulSoup
import re


def scraping():
    url = 'https://www.hogehoge.co.jp/company/news/'
    # The url you want to get.

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    elems = soup.find_all('a', class_='class__link')
    # Specify html elements and classes
    return str(elems[0].contents[0])+str(elems[0].attrs["href"])
