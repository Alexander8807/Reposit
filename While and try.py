while True:
    user_input = input("Please enter your id code: ")
    if len(user_input) != 11:
        print("Please try again")
        continue
    else:
        print(user_input)
        break


a = input("Please entered your id: ")
try:
    a = int(a)
except:                # можно добавить конкретную ошибку: TypeError
    print("ERROR")
else:
    print(a)
finally:
    print("Program stopped working")