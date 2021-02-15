def squares(number, multiplier):
    result = number ** multiplier  # вторая степень      25 ** 0,5  - корень из 25
    return (result)                # вернуть результат функции

x = 5
y = 3

print(squares(x, y))



def print_message(worker):
    return "Hello " + worker[0] + " " + worker[1] + ". You are " + worker[2] + " years old.\n" \
           "Your salary is " + str(worker[3]) + " EUR. You are on " + worker[4] + " position"

worker_data = ["John", "worker", "35", 2000, "programmer"]

print(print_message(worker_data))



def double(number):
    result = number * 2
    return result

def triple(number):
    result = number * 3
    return result

print(double(5))
print(triple(5))

print(double(5) + triple(7))



def create_string(name):
    result = "Hello " + name
    return result

print(create_string("Roman") + " How are you?")