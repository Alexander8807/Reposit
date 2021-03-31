from tkinter import *

root = Tk()  #создание окна программы

root.title("Squares calculator")  #заголовок программы

root.geometry("640x480")  #разрешение окна

#user_lable = Label(root, text="Please enter your name: ")
#user_lable.pack()
#user_entry = Entry(root, width=50, bg="black", fg="white", borderwidth=5)  # инпут для окна
#user_entry.pack()


#my_label = Label(root, text="This is my first label") #содержание программы
#my_label.pack()  #запихивает переменную в окно
#my_label.grid(row=1, column=1) #установка элемента в определенном месте в окне

#my_label2 = Label(root, text="This is my second label")
#my_label2.grid(row=0, column=0)

#my_label3 = Label(root, text="This is my third label")
#my_label3.grid(row=0, column=2)


#def myClick():
#    my_label = Label(root, text=user_entry.get()) #что будет при нажатии кнопки
#    my_label.pack()

#my_button = Button(root, text="Click me", command=myClick, fg="blue", bg="red", padx=50, pady=10)  #создание кнопки в окне
#my_button.pack()

root.mainloop()  #бесконечный цикл для окна (обновляет окно каждую секунду)
