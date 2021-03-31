from tkinter import *

root = Tk()
root.title("Graf")  #заголовок программы
root.geometry("640x480")

image1 = PhotoImage(file="Bryul.png")
my_label = Label(root, image=image1)
my_label.grid(row=0, column=2, columnspan=3)

user_entry = Entry(root, width=35, borderwidth=5)
user_entry.grid(row=1, column=2, columnspan=3)

def isiku():
    user_entry.delete(0, END)
    enter = True

    while enter:
        try:
            isikukood = int(input("Пожалуйста введите свой личный код: "))
        except:
            print("Вы ввели неверный символ.")
            continue
        else:

            isikukood = str(isikukood)

        try:
            num1 = int(isikukood[0]) * 1 + int(isikukood[1]) * 2 + int(isikukood[2]) * 3 + int(isikukood[3]) * 4 + int(
                isikukood[4]) * 5 + int(isikukood[5]) * 6 + int(isikukood[6]) * 7 + int(isikukood[7]) * 8 + int(
                isikukood[8]) * 9 + int(isikukood[9]) * 1
            num2 = int(isikukood[0]) * 3 + int(isikukood[1]) * 4 + int(isikukood[2]) * 5 + int(isikukood[3]) * 6 + int(
                isikukood[4]) * 7 + int(isikukood[5]) * 8 + int(isikukood[6]) * 9 + int(isikukood[7]) * 1 + int(
                isikukood[8]) * 2 + int(isikukood[9]) * 3
            num = int(isikukood[10])
        except:
            print("Вы ввели меньше символов.")
        else:

            if len(isikukood) == 11:
                if num1 % 11 == num:
                    print("Ваш личный код принят.")
                elif num1 % 11 == 0 and num2 % 11 == num:
                    print("Ваш личный код принят. 1")
                elif num1 % 11 != num and num2 % 11 != num:
                    print("Введен неверный личный код.")
                    continue
            elif len(isikukood) > 11:
                print("Вы ввели больше символов.")
                continue
            else:
                print("Вы ввели меньше символов.")
                continue

            male = int(isikukood[0])

            if male % 2 == 0:
                print("Вы женщина.")
            else:
                print("Вы мужчина.")

            century = int(isikukood[0])
            year = int(isikukood[1:3])
            month = int(isikukood[3:5])
            day = int(isikukood[5:7])

            if century == 1 or century == 2:
                century = 1800
            elif century == 3 or century == 4:
                century = 1900
            elif century == 5 or century == 6:
                century = 2000
                print("Ваша дата рождения: {}.{}.{}".format(day, month, century + year))

            town = int(isikukood[7:10])

            if town >= 1 and town <= 10:  # if town in range(1, 11):
                print("Вы родились в Kuressaare haigla.")  # region = "Kuressaare haigla"
            elif town >= 11 and town <= 19:
                print("Вы родились в Tartu Ülikooli Naistekliinik.")
            elif town >= 21 and town <= 150:
                print("Вы родились в Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn).")
            elif town >= 151 and town <= 160:
                print("Вы родились в Keila haigla.")
            elif town >= 161 and town <= 220:
                print("Вы родились в Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla).")
            elif town >= 221 and town <= 270:
                print("Вы родились в Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi).")
            elif town >= 171 and town <= 370:
                print("Вы родились в Maarjamõisa kliinikum (Tartu), Jõgeva haigla.")
            elif town >= 371 and town <= 420:
                print("Вы родились в Narva haigla.")
            elif town >= 421 and town <= 470:
                print("Вы родились в Pärnu haigla.")
            elif town >= 471 and town <= 490:
                print("Вы родились в Haapsalu haigla.")
            elif town >= 491 and town <= 520:
                print("Вы родились в Järvamaa haigla (Paide).")
            elif town >= 521 and town <= 570:
                print("Вы родились в Rakvere haigla, Tapa haigla.")
            elif town >= 571 and town <= 600:
                print("Вы родились в Valga haigla.")
            elif town >= 601 and town <= 650:
                print("Вы родились в Viljandi haigla.")
            elif town >= 651 and town <= 700:
                print("Вы родились в Lõuna-Eesti haigla (Võru), Põlva haigla.")

    my_label.grid(row=2, column=0)




my_button = Button(root, text="Isikukood", command=lambda: isiku())
my_button.grid(row=3, column=3)

root.mainloop()