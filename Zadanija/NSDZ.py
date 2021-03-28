import os
import time

os.chdir("./needs_sorting")
os.makedirs("images")
os.makedirs("text_files")

time.sleep(1)

for file in os.listdir():
    if file.endswith(".txt"):
        os.replace(file, "text_files/" + file)
    if file.endswith(".jpg") or  file.endswith(".jpeg") or file.endswith(".png"):
        os.replace(file, "images/" + file)


