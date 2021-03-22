from collections import Counter

sample_string = "aaaaaaaabbbbbbbbccccccdddddffffff"
my_counter = Counter(sample_string)
print(my_counter)        #словарь

print(my_counter["a"])  #сколько раз встречается a

print(my_counter.values()) #все количества

print(my_counter.keys())  #все ключи
print("\n")

print(my_counter.most_common())  #вывод счетчика в порядке убывания

print(list(my_counter.elements()))  #сделать список из элементов строки
