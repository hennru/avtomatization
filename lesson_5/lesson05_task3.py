from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

# Находим поле ввода и работаем с ним
input_field = driver.find_element(By.ID, "number")
input_field.send_keys("Sky")
input_field.clear()
input_field.send_keys("Pro")
sleep(5)
driver.quit()