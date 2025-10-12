import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Page Object для медленного калькулятора.

    :param driver: экземпляр WebDriver
    :type driver: selenium.webdriver.Chrome
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    @allure.step("Ожидаем готовность калькулятора")
    def wait_calculator_ready(self) -> None:
        """Ожидает появления кнопки '7' как признака готовности интерфейса."""
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[normalize-space()='7']")))

    @allure.step("Ввод задержки {value} сек")
    def input_delay(self, value: str) -> None:
        """Устанавливает задержку выполнения вычисления.

        :param value: число секунд в строковом виде
        :type value: str
        :return: None
        """
        el = self.wait.until(
            EC.visibility_of_element_located((By.ID, "delay")))
        el.clear()
        el.send_keys(value)

    @allure.step("Нажимаем цифру {number}")
    def press_number(self, number: str) -> None:
        """Нажимает кнопку с указанной цифрой.

        :param number: символ цифры (например, '7')
        :type number: str
        :return: None
        """
        btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[normalize-space()='{number}']")))
        btn.click()

    @allure.step("Нажимаем оператор {operator}")
    def press_operator(self, operator: str) -> None:
        """Нажимает кнопку оператора (например '+', '=', и т.д.).

        :param operator: строка-оператор
        :type operator: str
        :return: None
        """
        btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[normalize-space()='{operator}']")))
        btn.click()

    @allure.step("Читаем результат с экрана")
    def get_result(self) -> str:
        """Возвращает текст, который отображается на экране калькулятора.

        :return: текст с экрана
        :rtype: str
        """
        el = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.screen")))
        return el.text.strip()

    @allure.step("Ожидаем результат {expected_value}")
    def wait_for_result(self, expected_value: str, timeout: int = 60) -> None:
        """Ждёт, пока на экране появится ожидаемое значение.

        :param expected_value: ожидаемое текстовое значение
        :type expected_value: str
        :param timeout: таймаут в секундах
        :type timeout: int
        :return: None
        """
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_result() == expected_value)
