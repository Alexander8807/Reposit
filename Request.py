# 200 success      все ок
# 300 redirect     перенаправление
# 400 client       error ошибки кода
# 500 server       ошибки сервера

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
#зайти на сайт, обойдя защиту

r = requests.get("https://xkcd.com/353/", timeout=3, headers=headers)
print(r)
print(r.status_code) #проверить статус

print(r.text)   #показать код страницы

print(r.content)

p = requests.get("https://imgs.xkcd.com/comics/python.png", timeout=5)
with open("python.png", "wb") as file:
    file.write(p.content)  #картинка

print(r.ok) #запрос об ошибках

print(p.headers)  #информация о контенте