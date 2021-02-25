import pandas as pd   #импорт пандас и дать имя pd
import json

with open("oke.json", "r", encoding="UTF8") as file:  #работа с файлом json
    data = json.load(file)

df = pd.DataFrame(data["people"])   #создать обьект  DataFrame
print(df)
print(type(df))



df = pd.read_csv("Zadanija//TableHome.csv", header=1)      #пропустить заголовок
#работа с файлом csv     в качестве ключа берется 1 строка таблицы
#header=None  используется, если заголовков нет
#header=None, name=["Названия", "заголовков", "добавить"]
             #nrows=15 - количество рядов

pd.set_option("display.max_columns", 9) #установки колонок и строчек при отображении в ком строке
pd.set_option("display.max_rows", 157)

print(df)