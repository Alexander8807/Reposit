a = str(input("Enter your text: "))
a = a.lower()
a = a.replace(" ", "")
if a[0:] == a[::-1]:
    print("The text is a palindrome")
else:
    print("The text is not a palindrome")