import csv

#with open("Textcsv.csv", "r", encoding="UTF8") as csv_file:
    #csv_reader = csv.reader(csv_file)
    #print(csv_reader)

    #next(csv_reader)  #пропустить первый элемент списка (заголовки таблицы)

    #for line in csv_reader:
        #print(line)            #вывести форму таблицы, индексируется



with open("Textcsv.csv", "r", encoding="UTF8") as csv_file:
    csv_reader = csv.reader(csv_file)       #прочитать файл
   #csv_reader = csv.DictReader(csv_file)   прочитать файл, как словарь

    with open("Textcsv_copy.csv", "w", encoding="UTF8") as new_file:
        csv_writer = csv.writer(new_file, delimiter="*", lineterminator="\n")  #delimiter разделение столбцов, lineterminator чем закончить каждую линию
       #csv_writer = csv.writeheader()    записать заголовок
       #csv_writer = csv.DictWriter(new_file)   записать, как словарь

        for line in csv_reader:
            csv_writer.writerow(line)