import os
import time

os.chdir("./needs_sorting")
os.makedirs("images")
os.makedirs("text_files")

time.sleep(1)

a = []
b = []
for file in os.listdir():
    if file.endswith(".txt"):
        os.replace(file, "text_files/" + file)
    if file.endswith(".jpg") or  file.endswith(".jpeg") or file.endswith(".png"):
        os.replace(file, "images/" + file)


os.chdir("./text_files")
a.append(os.listdir("C:/Users/user/PycharmProjects/Reposit1/Zadanija/needs_sorting/text_files/"))
for file1 in os.listdir():
    a.append(os.stat(file1)[6])
    a.append(time.ctime(os.stat(file1)[8]))
with open("x_file.txt", "w", encoding="UTF8") as text_a_file:
    text_a_file.write(str(a))

os.chdir("../images")
b.append(os.listdir("C:/Users/user/PycharmProjects/Reposit1/Zadanija/needs_sorting/images/"))
for file1 in os.listdir():
    b.append(os.stat(file1)[6])
    b.append(time.ctime(os.stat(file1)[8]))
with open("y_file.txt", "w", encoding="UTF8") as image_b_file:
    image_b_file.write(str(b))


