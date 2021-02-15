num = input("Please enter your national ID: ")       # = присваивание, == равенство, != неравенство#

if len(num) == 11:
    print("Your ID code is", num)
elif len(num) > 11:
    print("Code you entered is longer")
else:
    print("Code you entered is shorter")

