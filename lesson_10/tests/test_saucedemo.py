import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.title("SauceDemo: оформление заказа")
@allure.description("Авторизация, добавление 3 товаров, оформление заказа и проверка итогового сообщения.")
@allure.feature("SauceDemo")
@allure.severity(allure.severity_level.NORMAL)
def test_saucedemo_checkout(driver):
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    with allure.step("Авторизация"):
        login.login("standard_user", "secret_sauce")

    with allure.step("Добавляем товары в корзину"):
        inventory.add_to_cart("Sauce Labs Backpack")
        inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory.add_to_cart("Sauce Labs Onesie")
        inventory.go_to_cart()

    with allure.step("Переходим к оформлению и заполняем данные"):
        cart.click_checkout()
        checkout.fill_form("Pavel", "Kirillov", "12345")
        checkout.finish_order()

    with allure.step("Проверяем сообщение об успешном заказе"):
        message = checkout.get_success_message()
        assert message in ("THANK YOU FOR YOUR ORDER",
                           "Thank you for your order!"), f"Неверное сообщение: {message}"
