import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Page Object страницы корзины."""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Нажимаем Checkout")
    def click_checkout(self) -> None:
        """Нажимает кнопку checkout на странице корзины.
        :return: None
        """
        self.driver.find_element(By.ID, "checkout").click()
