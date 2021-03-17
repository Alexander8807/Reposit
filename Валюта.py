from bs4 import BeautifulSoup as BS
import requests

def user_choice():
    try:
        user_input = input("Please choose:\n1. Convert RUB to EUR\n2. Convert EUR to RUB\n3. Exit\n--> ")

        if user_input == "1":
            amount = float(input("Please enter amount:\n--> "))
            result = amount * get_currency_value()
            print(result, "Euro")
            user_choice()
        elif user_input == "2":
            amount = float(input("Please enter amount:\n--> "))
            result = amount / get_currency_value()
            result_string = "{result:.2f} Rubles"
            print(result_string.format(result=result))
            user_choice()
        elif user_input == "3":
            print("Exit")
        else:
            print("Choice is out of range")
            user_choice()
    except:
        print("Error")
        user_choice()

def get_currency_value():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    url = "https://www.google.com/search?q=rub+to+eur&oq=rub+to+eur&aqs=chrome..69i57.4001j0j7&sourceid=chrome&ie=UTF-8"
    full_page = requests.get(url, timeout=3, headers=headers)
    soup = BS(full_page.content, "html.parser")
    currency_value = soup.findAll("span", class_="DFlfde SwHCTb")
    result = currency_value[0].text.replace(",", ".")
    return float(result)

user_choice()




