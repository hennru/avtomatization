from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class InventoryPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_to_cart(self, product_name: str):
        product_id = product_name.lower().replace(" ", "-")
        self.driver.find_element(By.ID, f"add-to-cart-{product_id}").click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()