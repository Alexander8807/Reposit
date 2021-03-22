import os
import time

#print(dir(os))  #показать все сетоды данной библиотеки

#print(os.getcwd()) #показать полный путь к папке с этим файлом

#os.chdir("../") #вернуться на папку назад
#os.chdir("./test") #в этой папке открыть файл test
#print(os.getcwd())

#print(os.listdir())  #показать список из файлов в текущей папке

#os.makedirs("new_folder/sub_folder/sub_folder1")   #создать папку
#time.sleep(5)  #время задержки между операциями 5 сек
#os.rmdir("new_folder/sub_folder/sub_folder1")      #удалить последнюю папку
#os.removedirs("new_folder/sub_folder/sub_folder1") #удалить все перечисленные папки
#os.rename("sample.txt", "text.txt")                #переименовать папку

#print(os.stat("text.txt"))          #информация о файле
#print(os.stat("text.txt").st_size)  #размер папки

#information = os.walk("C:/Users/user/PycharmProjects/Reposit1/")
#for dirpath, dirnames, filenames in information:
#    print("Current path: ", dirpath)
#    print("Directories: ", dirnames)  #сортировка содержимого по указанному пути
#    print("Files", filenames)
#    print()

#print(os.environ)  #информация о переменных в виде словаря  variables
#file_path2 = os.path.join(os.environ.get("ALLUSERSPROFILE"), "text.txt")
#print(file_path2)        #указан ключ одной из переменных

print(os.path.basename("C:/Users/user/PycharmProjects/Reposit1/БиблДир.py")) #название данного файла
print(os.path.dirname("C:/Users/user/PycharmProjects/Reposit1/БиблДир.py"))  #название папки данного файла
print(os.path.split("C:/Users/user/PycharmProjects/Reposit1/БиблДир.py"))    #разделяет показывает отдельно файл и его папку
print(os.path.exists("C:/Users/user/PycharmProjects/Reposit1/БиблДир.py"))   #проверка на существование данного пути
print(os.path.isdir("C:/Users/user/PycharmProjects/Reposit1/БиблДир.py"))   #проверка, правильная ли папка для этого файла
print(os.path.isfile("C:/Users/user/PycharmProjects/Reposit1/БиблДир.py"))  #проверка, правильный ли путь файла
print(os.path.splitext("C:/Users/user/PycharmProjects/Reposit1/БиблДир.py"))  #показывает отдельно файл и его расширение, проверка расширения файла
