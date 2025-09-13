from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get("http://uitestingplayground.com/ajax")
    
    # Находим и нажимаем кнопку
    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()
    
    # Добавляем явное ожидание появления сообщения
    wait = WebDriverWait(driver, 20)
    message = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    
    # Выводим текст сообщения
    print(message.text)  # Вывод: Data loaded with AJAX get request.
    
finally:
    driver.quit()