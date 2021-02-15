a_list = []
print(type(a_list))

a_tuple =()
print(type(a_tuple))

a_set = set()
print(type(a_set))         #типы список, кортеж#

some_list = [1243464, 123.00023, "Some string", True, None, [1234, "New string", False]]
print(some_list)                             #список внутри списка#
print(some_list[0:3])            #вывести список от 1 до 3 элемента#

courses = ["History", "Math", "Literature", "Physics", "Programming", [1, 2, 3, 4, 5]]
courses2 = ["Art", "Biology"]
print(courses[2][5:])     #сначала элемент, затем буква элемента#
print(courses)

courses[2] = "Art"             #заменить 3й элемент на арт#
print(courses)
print(len(courses))     #посчитать элементы списка#
print(courses + courses2)   #сложить списки#
courses.append("Art")          #добавить слово арт в список, можно добавить так же другой список#
print(courses)
courses[5].append(courses2)      #добавили список в шестой элемент#
print(courses)
courses.remove("Math")            #удалить слово Math из списка#
print(courses)

popped_item = courses.pop()
courses.pop()                  #выкинуть последний элемент и принять его значение#
print(courses)
print(popped_item)
courses.insert(2, "Geometry")       #Вставить на позицию 2го элемента слово Geometry#
print(courses)
courses.extend(courses2)           #сложение списков (лучше просто +)#
print(courses)

numbers = [1, 45, 63, 34, 56, 78, 3]
print(numbers)
numbers.sort()               #сортировка чисел по возрастанию#
print(numbers)                                                  #Смешанные списки нельзя сортировать#
courses.sort()               #сортировка элементов по алфавиту#
print(courses)
courses.sort(reverse=True)              #сортировка в обратном порядке#
print(courses)
print(sorted(courses))                 #показать единожды сортировку по возрастанию#
print(min(numbers))                    #показать минимальное число#
courses.sort(reverse=False)            #вернуть сортировку в порядок#
print(max(numbers))                    #показать максимальное число#
print(sum(numbers))                    #суммировать числа в списке#
print(courses.index("History"))        #индексация#

new_string = ", ".join(courses)         #конвертировать список в строку, перечесляя элементы списка через запятую и пробел#
print(new_string)

list_1 = ["Math", "History", "Programming", "Physics"]
list_2 = list_1.copy()                  #копировать, но в дальнейшем может измениться#
print(list_1)
print(list_2)
list_1[2] = "Sports"
list_2[0] = "Art"
print(list_1)
print(list_2)