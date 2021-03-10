
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
#зайти на сайт, обойдя защиту

from bs4 import BeautifulSoup as BS
import requests

r = requests.get("https://gammatest.net/course/python/")
soup = BS(r.content, "html.parser")
print(soup.prettify()) #показать код со всеми отступами

print(soup.title)  #вывести title сайта в виде текста
print(soup.title.text)  #только текст title

match = soup.findAll("div", class_="col-md-12 col-sm-12")  #поиск
print(match[0])  #получить все совпадения





