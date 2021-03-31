from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #Возможность нажимать кнопки
import time

driver_location = "chromedriver.exe"   #путь к файлу exe
driver = webdriver.Chrome(driver_location)  #подключение

driver.get("https://github.com")  #открыть данную ссылку


#time.sleep(7)
#driver.close()  #закрыть данную ссылку
#time.sleep(7)
#driver.quit()   #закрыть браузер


search = driver.find_element_by_name("user_email") #в коде страницы название элемента, с которым работаем
                #найти конкретный элемент по конкретному имени

#print(search.is_displayed())  #Видимый ли это элемент для пользователя, True или False
#print(search.is_enabled())    #Можно ли взаимодействовать с этим элементом
#print(search.is_selected())   #Выделен ли элемент курсора


if search.is_enabled() == True:
    print("All is good")
    search.send_keys("dkomop@oopjko.ee")  #введи данный текст
    search.send_keys(Keys.RETURN) #return = enter,  нажми ентер
else:
    print("Program crashed")

login = driver.find_element_by_id("user_login")
login.send_keys("Hello world")
time.sleep(5)
login.clear()   #очистить
login.send_keys("LearnPython")

print(driver.page_source) #получить HTML код данной страницы