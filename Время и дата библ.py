import calendar

print(calendar.calendar(2020, w=0, l=0, c=20, m=6))      #вывод календаря  w, l, c и m это отступы между календарей


print(calendar.isleap(2020))  #високосный год   true
print(calendar.isleap(2018))  #не високосный год  false
print(calendar.leapdays(2000, 2021))  #количество високосных лет в заданном диапазоне


import time

start = time.time()   #возьми время сейчас в переменную start
#time.sleep(7)        #пауза в 7 секунд в коде

end = time.time()      #возьми время сейчас в переменную end
print(end - start)     #посчитай разницу между ними в сек

print(time.asctime())   #вывод настоящего времени
print(time.gmtime())     #разбор времени подробно
print(type(time.gmtime()))  #тип времени

date_now = time.gmtime()
print(date_now[0], date_now[1], date_now[2])  #индексация времени


import datetime       #библиотека и даты и времени

d = datetime.date(2018, 7, 22)
print(d)

today = datetime.date.today()    #сегодняшняя дата
print(today)                  #он еще не строка, надо print(str(today))

d = datetime.date(2000, 6, 15)
today = datetime.date.today()
print(today - d)             #сегодня минус заданная дата

print(today.year)     #вывести сегодняшний год
print(today.day)      #вывести сегодняшний день
print(today.month)    #вывести сегодняшний месяц

print(today.weekday())        #понедельник = 0, воскресенье = 6
print(today.isoweekday())     #понедельник = 1, воскресенье = 7        как удобно

today = datetime.date.today()
delta = datetime.timedelta(days=7)  #сколько дней спустя (7)
print(today + delta)                #что будет через 7 дней

today = datetime.date.today()
bday = datetime.date(2021, 4, 21)
till_bday = bday - today
print(till_bday)               #сколько осталось до моего дня рождения

t = datetime.time(13, 24, 10, 10)
print(t)           #вывод заданного времени

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
print(dt_today)                #2 способа вывести время, одинаковые
print(dt_now)

dt_today = datetime.datetime.today()
print(dt_today.strftime("%B %d, %Y"))                 #формат вывода времени в виде строки, обозначения в интернете

dt_str = "November 30, 2020"
#dt_str = "Nov 30, 2020"
#print(dt_str)
str_to_date = datetime.datetime.strptime(dt_str, "%B %d, %Y")       #конвертация во время от строки
print(str_to_date)
print(type(str_to_date))
