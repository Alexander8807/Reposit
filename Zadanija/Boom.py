import math

def maxHL():
    while True:
        try:
            V0 = float(input("Введите начальную скорость снаряда: "))
            a = float(input("Введите угол запуска снаряда: "))
            g = float(input("Введите ускорение свободного падения снаряда: "))
        except:
            print("Вы ввели неверный символ, попробуйте еще")
            continue
        else:
            a = math.sin(math.radians(a))
            hmax = ((V0**2) * (math.sin(a) * math.sin(a))) / (2 * g)
            lmax = ((V0**2) * (2 * math.sin(a) * math.cos(a))) / g
            print("Максимальная высота полета вашего снаряда равна: " + str(hmax) + "\nМаксимальная длина полета вашего снаряда равна: " + str(lmax))
            exit()
maxHL()