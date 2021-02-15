set1 = {"Math", "History", "Programming", "Physics", "Math"}        #выводит элементы в случайном порядке, убирая все повторы#
set2 = {"Art", "Physics", "Design", "History"}                   #сет неизменяем, как список#
print(set1)

list1 = ["Math", "History", "Programming", "Physics", "Math", "History"]
print(list1)
print(type(list1))
print(list(set(list1)))

print(set1.intersection(set2))      #ищет элементы, которые есть в обоих сетах#
print(set2.difference(set1))      #найти различия между сетами#
print(set1.difference(set2))
print(set1.union(set2))            #обьеденить два сета в один#
