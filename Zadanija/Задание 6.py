a = [1, 2, 9, 3, 4, 7, 9, 4, 2, 4]
max_count = 0
b = []

for num in a:
    if a.count(num) > max_count:
        max_count = a.count(num)

for num in a:
    if a.count(num) == max_count:
        b.append(num)
b = list(set(b))
print(b)

