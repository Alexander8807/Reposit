from bs4 import BeautifulSoup as BS
import requests

def question():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    url = "https://www.google.com/search?sxsrf=ALeKk00Iu-ifxdlXNtlZYmWmIPK91ZN-bg:1615455461065&q=i%27m+feeling+curious&ved=2ahUKEwi10aDH-KfvAhW6AhAIHSQoCysQ73MwAHoECA8QAw"
    full_page = requests.get(url, timeout=3, headers=headers)
    soup = BS(full_page.content, "html.parser")
    question1 = soup.findAll("div", class_="sW6dbe")
    question1 = "Question:\n" + question1[0].text
    answer1 = soup.findAll("div", class_="DRBylb")
    answer1 = "Answer:\n" + answer1[0].text
    print(question1 + "\n" + answer1)

question()
