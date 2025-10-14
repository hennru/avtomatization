import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.calculator_page import CalculatorPage


@allure.title("Калькулятор: проверка 7 + 8 = 15")
@allure.description("Открываем slow-calculator, вводим delay=5, выполняем 7+8, проверяем результат 15.")
@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calc = CalculatorPage(driver)

    with allure.step("Ожидаем загрузки калькулятора"):
        calc.wait_calculator_ready()

    with allure.step("Вводим задержку и выражение"):
        calc.input_delay("5")
        calc.press_number("7")
        calc.press_operator("+")
        calc.press_number("8")
        calc.press_operator("=")

    with allure.step("Ожидаем и проверяем результат"):
        calc.wait_for_result("15")
        result = calc.get_result()
        assert result == "15", f"Ожидалось 15, получено {result}"
