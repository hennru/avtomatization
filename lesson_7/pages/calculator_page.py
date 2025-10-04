from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120)  # 2 минуты на загрузку

    def input_delay(self, seconds: str):
        delay_input = self.wait.until(EC.visibility_of_element_located((By.ID, "delay")))
        delay_input.clear()
        delay_input.send_keys(seconds)

    def wait_calculator_ready(self):
        # Ждём, пока кнопка "0" станет кликабельной
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-value="0"]')))

    def press_number(self, number: str):
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f'//button[text()="{number}"]'))
        )
        button.click()

    def press_operator(self, operator: str):
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f'//button[text()="{operator}"]'))
        )
        button.click()

    def get_result(self) -> str:
        result_elem = self.wait.until(EC.visibility_of_element_located((By.ID, "result")))
        return result_elem.text