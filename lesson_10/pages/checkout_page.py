import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Page Object страницы оформления заказа."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Заполняем данные покупателя: {first_name} {last_name}, {postal_code}")
    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Заполняет форму checkout (имя, фамилия, индекс) и нажимает Continue.

        :param first_name: имя
        :type first_name: str
        :param last_name: фамилия
        :type last_name: str
        :param postal_code: почтовый индекс
        :type postal_code: str
        :return: None
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Нажимаем Finish")
    def finish_order(self) -> None:
        """Завершает оформление заказа нажатием Finish.
        :return: None
        """
        self.driver.find_element(By.ID, "finish").click()

    @allure.step("Получаем сообщение об успешном заказе")
    def get_success_message(self) -> str:
        """Возвращает текст сообщения о завершении заказа.
        :return: str
        """
        el = self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")))
        return el.text.strip()
