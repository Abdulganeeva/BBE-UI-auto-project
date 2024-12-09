import pytest
from selenium import webdriver
from bbe.pages.cart_page import CartPage
from bbe.pages.order_page import OrderPage


@pytest.fixture(scope="class")
def init_driver(request):
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def cart_page(init_driver):
    return CartPage(init_driver)


@pytest.fixture(scope="class")
def order_page(init_driver):
    return OrderPage(init_driver)