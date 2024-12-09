import time

import allure
import pytest

from bbe.pages.start_page import StartPage


@pytest.mark.usefixtures("init_driver")
class TestMakeOrder:
    @allure.title("Тест создания заказа позитивный")
    def test_make_order_positive(self, cart_page, order_page):
        with allure.step('Инициализация страницы'):
            start_page = StartPage(self.driver)

        with allure.step('Открытие стартовой страницы'):
            start_page.open_start_page()

        with allure.step("Проверка того, что открыта главная страница"):
            start_page.page_tittle("ЮKassa")

        with allure.step('ID продукта, который хотим добавить в корзину'):
            product_id = '253354771'

        with allure.step('Добавление продукта в корзину'):
            start_page.add_product_to_cart(product_id)

        with allure.step('Проверка, что товар добавлен в корзину'):
            assert start_page.is_product_added_to_cart(), "Product was not added to cart"

        with allure.step('Переход на страницу Корзина'):
            start_page.cart_move()

        with allure.step("Проверка того, что мы находимся на странице Корзина"):
            cart_page.page_tittle("Корзина")

        with allure.step("Нажатие на кнопку Оформить заказ"):
            cart_page.click_make_order()

        with allure.step("Проверка того, что открыта cтраница оформления заказа"):
            start_page.page_tittle("Оформление заказа")

        with allure.step("Заполнение адреса"):
            order_page.make_address()

        with allure.step("Заполнение имени получаетля"):
            order_page.make_name()

        with allure.step("Заполнение номера телефона"):
            order_page.make_phone()

        with allure.step("Нажатие на кнопку Подтвердить заказ"):
            time.sleep(2)
            order_page.click_order_button()

    @allure.title("Тест создания заказа негативный")
    def test_make_order_negative(self, cart_page, order_page):
        with allure.step('Инициализация страницы'):
            start_page = StartPage(self.driver)

        with allure.step('Открытие стартовой страницы'):
            start_page.open_start_page()

        with allure.step("Проверка того, что открыта главная страница"):
            start_page.page_tittle("ЮKassa")

        with allure.step('ID продукта, который хотим добавить в корзину'):
            product_id = '253354771'

        with allure.step('Добавление продукта в корзину'):
            start_page.add_product_to_cart(product_id)

        with allure.step('Проверка, что товар добавлен в корзину'):
            assert start_page.is_product_added_to_cart(), "Product was not added to cart"

        with allure.step('Переход на страницу Корзина'):
            start_page.cart_move()

        with allure.step("Проверка того, что мы находимся на странице Корзина"):
            cart_page.page_tittle("Корзина")

        with allure.step("Нажатие на кнопку Оформить заказ"):
            cart_page.click_make_order()

        with allure.step("Проверка того, что открыта cтраница оформления заказа"):
            cart_page.page_tittle("Оформление заказа")

        with allure.step("Очистка поля Контактное лицо (ФИО)"):
            order_page.clear_name()

        with allure.step("Очистка поля Населенный пункт"):
            order_page.clear_address()

        with allure.step("Нажатие на кнопку Подтвердить заказ"):
            time.sleep(2)
            order_page.click_order_button()

        with allure.step("Проверка того, что появился текст ошибки у поля Населённый пункт"):
            address_error_element = order_page.find_address_error().text
            assert address_error_element == "Поле не заполнено"

        with allure.step("Проверка того, что появился текст ошибки у поля Контактное лицо (ФИО)"):
            name_error_element = order_page.find_name_error().text
            assert name_error_element == "Поле не заполнено"