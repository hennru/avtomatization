from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

# Вводим данные в поля и нажимаем кнопку
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.TAG_NAME, "button")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
login_button.click()

# Выводим текст с зеленой плашки
success_message = driver.find_element(By.CLASS_NAME, "flash").text
print(success_message)
sleep(5)
driver.quit()