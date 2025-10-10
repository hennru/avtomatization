from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск браузера
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

# Нажатие на кнопку
driver.find_element(By.CLASS_NAME, "btn-primary").click()

# Ожидание появления нужного текста
wait = WebDriverWait(driver, 40)  
text_elem = wait.until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "bg-success"),
        "Data loaded with AJAX get request"
    )
)

# Повторно ищем элемент, чтобы получить текст
text_element = driver.find_element(By.CLASS_NAME, "bg-success")
print(text_element.text)

driver.quit()