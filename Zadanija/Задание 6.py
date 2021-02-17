a = [1, 2, 9, 3, 4, 7, 9, 4, 2]
for i in range(len(a)):
    if not i == a.index(a[i]):
        print(a[i])
