courses = ["Math", "History", "Programming", "Physics", "Art", "Biology"]
counter = 0

for subject in courses:             #печать всех элементов в списке#
    print(subject)
    counter += 1               #добавлен счетчик#
    print(counter)

#courses2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#for num1 in courses2:
#    for num2 in courses2:
#        for num3 in courses2:
#            for num4 in courses2:
#                print(num1, num2, num3, num4)    #вывести всевозможные комбинации#

numbers = range(1, 100)
for num in numbers:
    if num % 2 == 0:
     print(num, "Even")
    else:
     print(num, "Odd")

numbers2 = range(1, 1000)
for num5 in numbers2:
    if num5 % 5 == 0 and num5 % 3 == 0:
        print(num, "FizzBuzz")
    elif num5 % 5 == 0:
        print(num, "Fizz")
    elif num5 % 3 == 0:
        print(num5, "Buzz")
