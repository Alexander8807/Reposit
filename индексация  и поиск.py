a = "Hello world world"
print(a[0])
print(a[0:5])      #двоеточие = от....до#
print(a[2:])
print(a[0::3])
print(a[::-1])  #индексация#

print(len(a))     #количество символов в а#

print(a.upper())  #все буквы текста заглавные#
print(a.lower())     #все буквы текста маленькие#
print(a.casefold())  #маленькие буквы с заменой нестандартных символов на стандартные#
print(a.capitalize())  #первая буква заглавная#

print("world" in a)  #найти слово world в строке а#
print(a.find("world"))   #найти первое слово world и найти его индекс#
print(a.count("world"))  #найти сколько раз в тексте а встречается слово world#
print(a.strip())        #убрать лишние пробелы с концов строки#

print(a.replace("world","people"))        #заменить world на people#

a = a.replace("world","people")           #заменить world на people навсегда#
print(a)