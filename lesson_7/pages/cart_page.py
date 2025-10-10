from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    checkout_button = (By.ID, "checkout")

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def get_cart_items(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]