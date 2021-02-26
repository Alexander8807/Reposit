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

#print(df.head())  #отобразить с заголовком, в скобках количество рядов (nrows)


#people = {

#    "first": ["Roman", "Bob", "John"],
#    "last": ["Kutselepa", "Smith", "Black"],   #словарь
#    "email":["mkkn@xample.com", "mkkn@xample.com", "mkkn@xample.com"]
#}

#df = pd.DataFrame(people) #перевод словаря в пандас
#print(df)
#print(df["email"])            #вывод мыла словаря


#print(df[["Country or region", "..."]])  #если хотим несколько столбцов, то список в списке


#print(df.iloc[5])  #выбрать ряд с заголовком вместе
#print(df.iloc[[0, 130, 28, 37], [5, 1, 7]])   #первый список это ряды, 2й список это столбцы
#print(df.iloc[0:16:2])  #каждый 2й в индексах от 0 до 16

#print(df.loc[[0, 130, 28, 37], ["Country or region", "Healthy life expectancy"]])  #столбцы только по названию, ряды по индексу

#print(df.shape)  #вывести количество рядов и столбцов (кортеж)

#print(df[["Country or region", "Score"]].value_counts()) #получить все значения 1го столбца (сколько раз встреч одинаковые значения)


#print(df.loc[0:16, "Country or region": "Freedom to make life choices"]) #указать срез столбца

#print(df.sort_values("Social support")) #сортировка столбика

#df.to_csv("pandas.csv")  #сохранить таблицу в файл

#df.to_csv("pandas.csv", columns=["Country or region", "Score"])  #Сохранить конкретные столбики

#a = df.rename(columns={"Social support": "Hello world"}) #переименовать столбик
