import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge(service=EdgeService(
        "C:/WebDriver/msedgedriver.exe"))
    wait = WebDriverWait(driver, 30)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        fields_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro",
            # zip оставляем пустым
        }

        # Заполняем поля
        for name, value in fields_data.items():
            input_elem = wait.until(
                EC.presence_of_element_located((By.NAME, name)))
            input_elem.clear()
            input_elem.send_keys(value)

        # Нажимаем Submit
        submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type=submit]"))
        )
        submit_button.click()

        # Ждём появления alert
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert")))

        # Проверяем Zip (должен быть красным)
        zip_code = wait.until(
            EC.presence_of_element_located((By.ID, "zip-code")))
        assert "alert-danger" in zip_code.get_attribute(
            "class"), "Zip code не подсвечен красным!"

        # Проверяем остальные поля на зелёную подсветку после сабмита
        for name in fields_data.keys():
            input_elem = wait.until(
                EC.presence_of_element_located((By.NAME, name)))
            parent_div = input_elem.find_element(By.XPATH, "..")
            border_color = parent_div.value_of_css_property("border-color")
            assert "rgb(40, 167, 69)" in border_color, f"Поле {name} не подсвечено зелёным!"

    finally:
        driver.quit()
