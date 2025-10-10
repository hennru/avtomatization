from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

# Вводим текст
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

# Нажимаем кнопку
button = driver.find_element(By.ID, "updatingButton")
button.click()

# Получаем и печатаем текст кнопки
print(button.text)  # "SkyPro"

driver.quit()