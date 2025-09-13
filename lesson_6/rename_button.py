from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get("http://uitestingplayground.com/textinput")
    
    # Добавляем ожидание появления поля ввода
    wait = WebDriverWait(driver, 20)
    input_field = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control"))
    )
    
    # Ввод текста в поле
    input_field.send_keys("SkyPro")
    
    # Находим и нажимаем кнопку
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
    )
    button.click()
    
    # Ждем изменения текста кнопки
    updated_button = wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "button.btn-primary"), 
            "SkyPro"
        )
    )
    
    # Выводим текст кнопки
    print(updated_button.text)  # Вывод: SkyPro
    
finally:
    driver.quit()