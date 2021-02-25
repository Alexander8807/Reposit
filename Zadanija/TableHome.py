import csv

with open("TableHome.csv", "r", encoding="UTF8") as homefile:
    csv_reader = csv.reader(homefile)
    next(csv_reader)
    next(csv_reader)

    for line in csv_reader:
        socsup = line[4]
        socsup = str.split(socsup)

        for num in socsup:
            print(socsup)






















