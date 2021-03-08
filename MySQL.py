import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  #путь к базе данных.
    user="root",       #имя пользователя в БД
    passwd="65433785a",  #пароль БД
    database="testdb"  #название БД, с которой работаем
)

mycursor = mydb.cursor()   #создание окна в myscl

#mycursor.execute("CREATE DATABASE testdb")  #создать БД


#mycursor.execute("SHOW DATABASES")  #
#for db in mycursor:              #показать содержимое БД
#    print(db[0])


#mycursor.execute("CREATE TABLE students (nane VARCHAR(255), age INTEGER(10))") #создать конкретную таблицу в БД

#mycursor.execute("SHOW TABLES")
#for table in mycursor:        #показать таблицу
#    print(table[0])

#student1 = [("John", 32), ("Roman", 36), ("Jane", 41), ("Max", 33)]
#nane = "Mary"
#age = 25
#sqlquery = "INSERT INTO students (nane, age) VALUES (%s, %s)"
#mycursor.executemany(sqlquery, student1)         #ввести быстро данные в таблицу mysql
#mydb.commit()

##mycursor.execute("INSERT INTO students (nane, age) VALUES ('" + nane + "', "+ str(age) + ")")  #в ковычках правила MYSQL
##mydb.commit() #поместить информацию в ДБ

#mycursor.execute("SELECT * FROM students")
#myresult = mycursor.fetchall() #прочитать все результаты БД после данной операции
#for student in myresult:
#    print("Hello " + student[0] + ". You are " + str(student[1]) + " years old.")

#myresult = mycursor.fetchone()
    #читает одно значение, если еще раз это написать, возмет следующее значение
#while myresult != None:
#    print(myresult)
#    myresult = mycursor.fetchone()

#sqlformula = "SELECT * FROM students WHERE nane > %s"
#mycursor.execute(sqlformula, ("30",)) #нужен кортеж,  (запятая)
#myresult = mycursor.fetchall()
#for res in myresult:
#    print(res)



import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",  #путь к базе данных.
    user="root",       #имя пользователя в БД
    passwd="65433785a",  #пароль БД
    database="testdb"  #название БД, с которой работаем
)

df = pd.read_sql_query("SELECT * FROM students", mydb)
print(df)        #конвертация таблицы из БД в дата фрейм (пандас)
print(type(df))