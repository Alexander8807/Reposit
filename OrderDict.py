from collections import OrderedDict

order_dict = OrderedDict()
order_dict["Name"] = "Jack"
order_dict["Surname"] = "Smith"
order_dict["Age"] = 30

print(order_dict)    #создание словаря


from collections import defaultdict

default_dict = defaultdict(int)  #по умолчанию тут инт
default_dict["a"] = 100
default_dict["b"] = 200
print(default_dict["c"])


from collections import deque

d = deque()
d.append(1)
d.append(2)
print(d)     #создать список

d.appendleft(3)  #добавить 3 в список
print(d)

d.extend([4, 5, 6])  #соединить список d со списком [4, 5, 6]
print(d)

d.rotate(1)  #сдвинуть список на 1 элемент
print(d)