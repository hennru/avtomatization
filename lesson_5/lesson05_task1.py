from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

# Находим кнопку по CSS-классу и кликаем
blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
blue_button.click()
sleep(5)
driver.quit()