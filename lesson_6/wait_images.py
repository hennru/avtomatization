from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 15)

# Ждём, пока третий <img> станет загруженным
third_img = wait.until(
    EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
)

# Ждём, пока у тега <img> появится непустой src
wait.until(lambda d: third_img.get_attribute("src") != "")

print(third_img.get_attribute("src"))

driver.quit()