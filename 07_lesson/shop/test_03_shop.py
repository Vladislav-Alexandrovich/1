import pytest
from selenium import webdriver

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop():
    Auth_Page = AuthPage(driver)
    login = "standard_user"
    password = "secret_sauce"
    Auth_Page.fill_login_fields(login, password)

    Main_Page = MainPage(driver)
    Main_Page.put_in_cart()

    Cart_Page = CartPage(driver)
    Cart_Page.checkout()

    Order_Page = OrderPage(driver)
    Order_Page.fill_order_details("Владислав", "Шахов", "188300")

    total_price = Order_Page.get_total_price()
    expected_price = "Total: $58.29"

    assert total_price == expected_price

    driver.quit()
