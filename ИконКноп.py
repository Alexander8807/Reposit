from tkinter import *

root = Tk()
root.title("Squares calculator")
root.geometry("640x480")
#root.iconbitmap("python_icon.ico") #иконка окна


image1 = PhotoImage(file="python.png") #картинка в переменной
my_label = Label(root, image=image1)
my_label.grid(row=0, column=3, columnspan=2)
quit_button = Button(root, text="Exit", command=root.quit) #кнопка выхода из программы
quit_button.grid(row=1, column=2)


#frame = LabelFrame(root, text="This is frame", padx=50, pady=50)
#frame.grid(row=0, column=3)  #миниокно в окне

#button = Button(frame, text="Click Me") #кнопка внутри миниокна frame
#button.pack()


#choice = IntVar()  #создание кнопок выбора 1(числовая переменная)
#choice.set("2")

#def choice_done(value):
#    my_label = Label(root, text=value).pack()

#Radiobutton(root, text="Choice1", variable=choice, value=1, command=lambda:choice_done(choice.get())).pack()
#Radiobutton(root, text="Choice2", variable=choice, value=2, command=lambda:choice_done(choice.get())).pack()
#Radiobutton(root, text="Choice3", variable=choice, value=3, command=lambda:choice_done(choice.get())).pack()

#my_label = Label(root, text=choice.get()).pack()


#modes = [
#    ("One", "One"),
#    ("Two", "Two"),
#    ("Three", "Three"),
#    ("Four", "Four")
#]

#choice = StringVar()  #текстовая переменная
#choice.set("One")

#for text, mode in modes:
#    Radiobutton(root, text=text, variable=choice, value=mode).pack()

#def choice_done(value):
#    my_label = Label(root, text=value).pack()
#    display_text.set = value

#display_text = StringVar()
#my_label = Label(root, text=display_text).pack()
#my_button = Button(root, text="Click me", command=lambda: choice_done(choice.get())).pack()


#def show_check_status():    #кнопка с галочкой
#    my_label = Label(root, text=var.get()).pack()

#var = StringVar()
#chk_box = Checkbutton(root, text="Check me", variable=var, onvalue="ON", offvalue="OFF")
#chk_box.deselect()
#chk_box.pack()

#my_label = Label(root, text=var.get()).pack()
#my_button = Button(root, text="Show check status", command=show_check_status).pack()


from tkinter import messagebox   #создание всплывающего окна (окно ошибки)

#def clicked():
#    responce = messagebox.askyesnocancel("This is error message", "This is a body of an error message")
                         #.showinfo
                         #.showquestion
                         #.showerror
#    Label(root, text=responce).pack()
#    if responce == 1:
#        Label(root, text="You clicked yes button").pack()
#    else:
#        Label(root, text="You clicked no button").pack()

#Button(root, text="Click me", command=clicked).pack()



#def show():         #кнопки выбора
#    my_label = Label(root, text=dropdown.get()).pack()

#menu_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#dropdown = StringVar()
#dropdown.set("Mon")  #выбор по умолчанию
#dropdown_menu = OptionMenu(root, dropdown, *menu_list)
#dropdown_menu.pack()

#my_button = Button(root, text="Show selection", command=show).pack()


root.mainloop()
