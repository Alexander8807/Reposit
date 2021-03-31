from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #Возможность нажимать кнопки
import time

driver_location = "chromedriver.exe"   #путь к файлу exe
driver = webdriver.Chrome(driver_location)  #подключение

driver.get("https://www.gammatest.net/")  #открыть данную ссылку

time.sleep(1)
link = driver.find_element_by_xpath("""//*[@id="hp"]/div[1]/div[3]/div[1]/p[2]/a""")
link.click()

#time.sleep(3)
#link2 = driver.find_element_by_link_text("Rohkem infot") #искать по тексту
#link2.click()

elements = driver.find_elements_by_tag_name("td")  #найти теги элемента
for element in elements:
    print(element.text)

time.sleep(2)
driver.back() #вернуться на страницу назад
time.sleep(2)
driver.forward() #вернуться на страницу вперед


python_link = driver.find_element_by_xpath('''//*[@id="hp"]/div[1]/div[2]/div/div[1]/a''')
python_link.click()
russian = driver.find_element_by_link_text("На русском")
russian.click()