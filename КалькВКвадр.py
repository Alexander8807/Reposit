from tkinter import *

root = Tk()
root.title("Squares calculator")
root.geometry("640x480")

user_entry = Entry(root, width=35, borderwidth=5) #поле ввода
user_entry.grid(row=0, column=0, columnspan=3) #место положения поля ввода
my_label = Label(root, text="Answer: ")

def get_squares(number):
    user_entry.delete(0, END) #очистить строку
    user_entry.insert(0, int(number) ** 2)
    my_label = Label(root, text=int(number) ** 2)
    my_label.grid(row=1, column=0)

my_button = Button(root, text="Count squares", command=lambda: get_squares(user_entry.get()))
my_button.grid(row=0, column=3)


root.mainloop()