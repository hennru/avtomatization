import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Page Object для страницы авторизации SauceDemo."""

    def __init__(self, driver: WebDriver):
        """Инициализация.
        :param driver: WebDriver
        :type driver: selenium.webdriver.Chrome
        """
        self.driver = driver

    @allure.step("Выполняем вход как {username}")
    def login(self, username: str, password: str) -> None:
        """Вводит логин/пароль и нажимает кнопку логина.

        :param username: имя пользователя
        :type username: str
        :param password: пароль
        :type password: str
        :return: None
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
