import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from pages.calculator_page import CalculatorPage

def test_calculator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calc = CalculatorPage(driver)
    calc.wait_calculator_ready()

    calc.input_delay("45")
    calc.press_number("7")
    calc.press_operator("+")
    calc.press_number("8")
    calc.press_operator("=")

    WebDriverWait(driver, 60).until(lambda d: calc.get_result() != "")
    assert calc.get_result() == "15"

    driver.quit()