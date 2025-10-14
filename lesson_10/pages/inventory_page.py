import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """Page Object главной страницы магазина (inventory)."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавляем в корзину товар: {product_name}")
    def add_to_cart(self, product_name: str) -> None:
        """Добавляет товар в корзину по видимому названию.

        :param product_name: точное название товара на странице
        :type product_name: str
        :return: None
        """
        btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")))
        btn.click()

    @allure.step("Переходим в корзину")
    def go_to_cart(self) -> None:
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
