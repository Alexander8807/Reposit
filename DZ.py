import csv

def sort_value(some_list):
    return (sorted(some_list, key=lambda x: x[2], reverse=True))

data_list = []
with open("TableHome.csv", "r", encoding="UTF8") as homefile:
    next(csv_file)
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        data_list.append(line)

result_list = []
for x in data_list:
    result_list.append([x["Overall rank"], x["Country or region"], x["GDP per capita"]])
print(sort_value(result_list))




def square(x):
    result = x * x
    return result

square2 = lambda x: x * x
print(square2(5))
print(type(square()))