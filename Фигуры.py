place = ["A1"] # input

letters = ["A", "B", "C", "D"]
numbers = ["1", "2", "3", "4"]
a = []

for letter in letters:
    for num in numbers:
        if place[0][0] != letter and place[0][1] != num:
            place1 = [letter + num]   # Находит все варианты и превращает в список
            a.append(place1[0])
            print(a)










