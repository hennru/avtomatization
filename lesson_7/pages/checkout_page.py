from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_info(self, first_name: str, last_name: str, postal_code: str):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total(self) -> str:
        total_text = self.driver.find_element(*self.total_label).text  # "Total: $58.29"
        return total_text.replace("Total: $", "")  # возвращаем только "58.29"