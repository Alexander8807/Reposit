dictionary = {"name": "Roman", "age": 32}  #ключ : значение. По индексу к словарю нельзя обращаться
print(dictionary["name"])

x = 5
student = {"name1": "John", "age": 32, "courses": ["Math", "Art", "Programming"], 1: "int key", 0.2: "float key", x: "variable",
           "var key": x}           #различные типы ключей и значений
print(student[x])
print(student[5])
print(student["var key"])

print(student.get("job", "ERROR"))      #вывести несуществующий ключ job c пометкой ERROR, в дальнейшем можно дать значение ключу

x = range(0, 10)
student = {"name": "John", "age": 32, "courses": ["Math", "Art", "Programming"], 1: "int key", 0.2: "float key", x: "variable",
           "var key": x}
print(student)
student["name"] = "Jack"       #изменение значения ключа
print(student)

student.update({"name": "Michael", "age": 27, "phone": "555-5555"})      #обновить данные словаря
print(student)

del student["name"]   #удаление ключа из словаря
print(student)

popped_item = student.pop("age")       #удаление ключа age, но сохранение его значения 27
print(popped_item)
print(student)

x = range(0, 10)
student = {"name": "John", "age": 32, "courses": ["Math", "Art", "Programming"], 1: "int key", 0.2: "float key", x: "variable",
           "var key": x}
print(student.keys())            #получить все ключи
print(student.values())          #получить все значения словаря
print(student.items())           #получить все ключи и значения

for key, value in student.items():  #для ключа и значения в ключах и значениях
    print(key, value)

some_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for x, y, z in some_list:  #присвоить каждому элементу списка свои переменные x, y, z
    print(x, y, z)