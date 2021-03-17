import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc
hall mall wall ball
'''

sentence = 'Start a sentence and then bring it to an end'

#pattern = re.compile(r"\D") #ищи все, кроме цифр
#pattern = re.compile(r"\d") #ищи цифру от 0 до 9
#pattern = re.compile(r"\d\d\d") #ищи цифру от 0 до 9, в три цифры подряд
#pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d") #ищи номера телефонов
#pattern = re.compile(r"\d{3}.\d{3}.\d{4}")  #в фигурных скобках количество цифр
#pattern = re.compile(r"\w{5,8}") #диапазон от 5 до 8 совпадений букв подряд
#pattern = re.compile(r"\d\d\d[-*]\d\d\d[-*]\d\d\d\d") #ищи номер телефона с тире, либо звездочкой
#pattern = re.compile(r"[89]\d\d\d[-*]\d\d\d[-*]\d\d\d\d") #ищи номер телефона, начинающийся с 8 или 9
#pattern = re.compile(r"[1-5]") #ищи цифру от 1 до 5
#pattern = re.compile(r"[a-zA-Z]") #ищи совпадения всех букв
#pattern = re.compile(r"[^a-zA-Z]") #ищи все, кроме совпадения всех букв
#pattern = re.compile(r"[^w]all")  #ищи слова с all, где первая буква не w
#pattern = re.compile(r"end$") #ищи End в конце строки
#pattern = re.compile(r"^Start") #ищи Start в начале строки
#pattern = re.compile(r"\bHa") #совпадения Ha, с которых начинается слово
#pattern = re.compile(r"\BHa") #ищи все совпадения Ha, с которых не начинается слово
#pattern = re.compile(r"\S") #ищи все знаки кроме пробелов, табуляции и переносов строк
#pattern = re.compile(r"\s")  #ищи все пробелы, табуляции и переносы строк
#pattern = re.compile(r".") #найти совпадение всех символов, в тексте вместо точки может быть любой знак
#pattern = re.compile(r"\.") #найти совпадения только точек
#pattern = re.compile(r"abc") #ищи в тексте abc (шаблон для поиска)  r = сырая строка
pattern = re.compile(r"M(rs|s|r)\.?[ ][A-Z]\w*") #группировка, ? = один символ или ни одного, * = от 0 и более индекс
# Mr., Mrs., Ms. _ точка или нет _ пробел _ Имя с большой буквы

matches = pattern.finditer(text_to_search) #найти и создать все обьекты, список
for match in matches:                      #span = индексы найденного
    print(match)
    #print(match.start(), match.end(), match.group())  #вывести стартовый и конечный индексы
print("\n")

pattern2 = re.compile(r"(\d{3}).(\d{3}).(\d{4})")# в виде кортежа, если в круглых скобках
matches2 = pattern2.findall(text_to_search) #находит все и дает в виде списка
print(matches2)
print("\n")

pattern3 = re.compile(r"bring")
matches3 = pattern3.search(sentence) #ищи в строке sentence слово bring
print(matches3)
print("\n")

pattern4 = re.compile(r"Start", re.IGNORECASE) #игнорируй размер букв, флаг
#pattern4 = re.compile(r"n$", re.MULTILINE) #ищи заканчивающиеся на n

matches4 = pattern4.search(sentence)
print(matches4)
print("\n")

emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk
example@example.org
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
'''

#pattern1 = re.compile(r"[a-zA-Z0-9][a-zA-Z0-9_\-\.]+@[a-zA-Z0-9\-]+\.\w{2,3}(\.\w{2,3})?") # + = от 1 и более символов, поиск мыла
pattern1 = re.compile(r"(http://|https://)?(www\.)?((\w|-)+)(\.\w+)") #поиск ссылок, дополнительные скобки это группы

#subbed_urls = pattern1.sub(r"\4", urls) #вывод групп в скобках выше
#print(subbed_urls)

matches1 = pattern1.finditer(urls)
for match1 in matches1:
    print(match1.group(1))  #вывод по группам в скобках
