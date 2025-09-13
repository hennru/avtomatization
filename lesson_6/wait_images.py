from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    driver.maximize_window()
    
    wait = WebDriverWait(driver, 30)
    
    # Ожидание загрузки DOM и изображений
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    wait.until(lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3)
    
    images = wait.until(lambda d: [
        img for img in d.find_elements(By.TAG_NAME, "img") 
        if img.is_displayed() and img.get_attribute('src')
    ])
    
    # Проверка и получение третьей картинки
    if len(images) >= 4:
        third_image = images[3]
        
        
        print(f"Значение src: {third_image.get_attribute('src')}")
    else:
        print(f"Найдено изображений: {len(images)}. Требуется минимум 3")

finally:
    driver.quit()