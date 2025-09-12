from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

# Находим кнопку по тексту и кликаем
blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
blue_button.click()
sleep(5)
driver.quit()