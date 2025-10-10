from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def wait_calculator_ready(self):
        # Ждём, пока появится кнопка "7" — индикатор готовности калькулятора
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='7']")))

    def input_delay(self, value: str):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)

    def press_number(self, number: str):
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[normalize-space()='{number}']"))
        )
        btn.click()

    def press_operator(self, operator: str):
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[normalize-space()='{operator}']"))
        )
        btn.click()

    def get_result(self) -> str:
        elem = self.driver.find_element(By.CSS_SELECTOR, "div.screen")
        return elem.text.strip()

    def wait_for_result(self, expected_value: str, timeout: int = 60):
        # Ждём, пока на экране появится нужный результат
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_result() == expected_value,
            message=f"Результат не стал равен {expected_value}"
        )