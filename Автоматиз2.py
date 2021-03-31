from selenium import webdriver
from selenium.webdriver.common.by import By  #Тип элемента
from selenium.webdriver.support.ui import WebDriverWait  #альтернатива
from selenium.webdriver.support import expected_conditions as EC  #проверка на существование элемента

driver_location = "chromedriver.exe"   #путь к файлу exe
driver = webdriver.Chrome(driver_location)  #подключение
driver.get("https://github.com")

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/main/div/div[1]/div[1]/div[1]/div/div/div[1]/h1"))) #10 sec
    print(element.text)  #вывод написанного на странице
except:
    quit()