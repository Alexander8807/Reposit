import  itertools

counter = itertools.count() #создать счетчик
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print("\n")


data = [100, 200, 300, 400]

data_sample = zip(itertools.count(), data)  #соединить список со счетчиком
for x in data_sample:
    print(x)
print("\n")


data_sample2 = itertools.zip_longest(data, range(10)) #на протяжении 10ти выводов, до самого длинного
for x in data_sample2:
    print(x)
print("\n")


counter = itertools.count(start=5, step=2)  #начни с 5 шагом 2
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print("\n")


counter = itertools.cycle(("On", "Off")) #светофор
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print("\n")

counter = itertools.repeat(4, times=3)  #повторить 3 раза
print(next(counter))
print(next(counter))
print(next(counter))
print("\n")


counter = itertools.repeat(4, times=3)
def squared(y):
    return y ** 2
result = map(squared, range(10))
print(list(result))

result2 = itertools.starmap(pow, [(5, 2), (1, 2), (2, 2)])  #возведение в степень
print(list(result2))
print("\n")

letters = ["a", "b", "c", "d"]
numbers = [0, 1, 2, 3]
names = ["Jack", "John"]

result = itertools.combinations(letters, 2) #комба из леттерса из 2 символов
                  #.permutations   упорядоченнная комба
                  #.product(letters, repeat=2)  всевозможные комбы
                  #.combinations_with_replacement(numbers, 4)  всевозможные комбы, неповторяющиеся никак
for x in result:
    print(x)
print("\n")


def more_than_two(x):
    if x > 2:
        return True
    return False

letters = ["a", "b", "c", "d"]
numbers = [1, 2, 3, 4]
numbers2 = [4, 5, 4, 3, 2, 1, 0, 4]
selectors = [True, True, False, True]
result = itertools.compress(letters, selectors)  #выводит ток тру
for item in result:
    print(item)

result2 = filter(more_than_two, numbers)  #фильтр
for x in result2:
    print(x)

result = itertools.dropwhile(more_than_two, numbers2)   #не реагируй, пока не найдешь false, дальнейшее покажи
                  #.takewhile(more_than_two, numbers2)    #наоборот, выведи все, что до false
for item in result:
    print(item)

result = itertools.accumulate(numbers2)   #выводить сумму 1 и 2 эл, затем 1, 2 и 3 эл, и т.д.
for x in result:
    print(x)
    