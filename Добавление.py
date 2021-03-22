def squared(x):
    return x ** 2

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(squared, int_list)))   #добавить в список результат функции

print([squared(x) for x in int_list if x % 2 == 0])  #добавь в список результат функции
print("\n")

data1 = [100, 200, 300, 400, 500, 600, 700]
data2 = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

combination = list(zip(data1, data2))     #присвоить значением из 1го списка значения из другого списка
combination2 = list(zip(data2, range(10)))
print(combination)
print(combination2[5][0])