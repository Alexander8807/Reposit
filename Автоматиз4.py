from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  #
import time

driver_location = "chromedriver.exe"   #путь к файлу exe
driver = webdriver.Chrome(driver_location)  #подключение
driver.get("https://particle-clicker.web.cern.ch/")

driver.implicitly_wait(5)

clicker_object = driver.find_element_by_id("detector-events")

#actions = ActionChains(driver)
#actions.click(clicker_object)
#cnt = 0                          #кликать по экрану
#while cnt < 100:
#    actions.perform()
#    cnt += 1

