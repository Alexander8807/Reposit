file = open("text.txt", "r", encoding="UTF8") #присвоить открытие файла переменной с указанием пути, тип read, кодировка UTF8
print(file.name)       #вывести название файла
print(file.mode)       #вывести режим файла read
print(file.closed)     #вывести состояние файла. Открыт False, закрыт True
file.close()           #закрыть файл
print(file.closed)

with open("text.txt", "r", encoding="UTF8") as file:  #открой путь к файлу и назови его переменной file
    print(file)
    print(file.closed)
print(file.closed)

with open("text.txt", "r", encoding="UTF8") as file:
    data = file.read()     #читает файл полностью и выводит в виде строки
    #data = file.readlines()    #читает файл и делает из абзацев список       #файл читается только 1 раз
    #data = file.readline()     #читает файл и выводит первый абзац, если повторить эту команду напечатает второй абзац и т.д.
    print(data)
    print(type(data))

    data1 = file.read()
    file.seek(0)          #напечатай файл снова с 0 индекса
    data2 = file.read()
    print(data2)

with open("text.txt", "r", encoding="UTF8") as file:
    data = file.read(1000)         #напечатай 1000 символов из файла и закончи его символами *******
    print(data, end="*******")

with open("text.txt", "r", encoding="UTF8") as file:
    for line in file:              #напечатай построчно файл
        print(line)

with open("text.txt", "r", encoding="UTF8") as file:
    size_to_read = 100                     #выводи по 100 символов
    file_content = file.read(size_to_read)
    while len(file_content) > 0:
        print(file_content, end="*****")     #через каждые 100 символов текста выводи *****
        print(len(file_content))
        file_content = file.read(size_to_read)

                               # Запись файла

string_variable = "Hello world "
with open("text3.txt", "w", encoding="UTF8") as file:  #создай файл text3 и напиши там Hello world 2 раза
    file.write(string_variable)
    file.write("Hello world!")

with open("text3.txt", "a", encoding="UTF8") as file:  #добавить в файл запись в конец
    file.write("Good bye")

with open("text3.txt", "w", encoding="UTF8") as file:
    file.write("Hello world")
    file.seek(0)           #заменить в Hello world с нулевого индекса буквы на Good
    file.write("Good" + "")

                               # Копирование 1 файла в другой, можно использовать if и т.д.
with open("text.txt", "r", encoding="UTF8") as rfile:
    with open("text_copy.txt", "w", encoding="UTF8") as wfile:
        for line in rfile:
            wfile.write(line)