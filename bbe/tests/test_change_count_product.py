import time

import allure
import pytest

from bbe.pages.start_page import StartPage


@pytest.mark.usefixtures("init_driver")
class TestChangeCountProduct:
    @allure.title("Тест на увелечение количество товара в корзине")
    def test_plus_product_from_card(self, cart_page):
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

        with allure.step("Получение количество товара"):
            count_product_before_click = cart_page.get_count_product()

        with allure.step("Нажатие на иконку плюса"):
            cart_page.click_plus()

        with allure.step("Получение количество товара"):
            count_product_after_click = cart_page.get_count_product()

        with allure.step("Проверка того, что колиство товара увечилось"):
            count_product_before_click += 1
            assert count_product_before_click == count_product_after_click
            time.sleep(10)

    @allure.title("Тест на уменьшение товара в корзине")
    def test_minus_product_from_card(self, cart_page):
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

        with allure.step("Нажатие на иконку плюса"):
            for i in range(10):
                cart_page.click_plus()

        with allure.step("Получение количество товара"):
            count_product_before_click = cart_page.get_count_product()

        with allure.step("Нажатие на иконку минуса"):
            cart_page.click_minus()

        with allure.step("Получение количество товара"):
            count_product_after_click = cart_page.get_count_product()

        with allure.step("Проверка того, что колиство товара уменьшилось"):
            count_product_before_click -= 1
            assert count_product_before_click == count_product_after_click

    @allure.title("Тест того, что колиство товара не может быть меньше 1")
    def test_min_count_product_from_card(self, cart_page):
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

        with allure.step("Получение количество товара"):
            count_product_before_click = cart_page.get_count_product()

        with allure.step("Нажатие на иконку минуса"):
            for i in range(count_product_before_click+1):
                cart_page.click_minus()

        with allure.step("Получение количество товара"):
            count_product_after_click = cart_page.get_count_product()

        with allure.step("Проверка того, что колиство товара не может быть меньше 1"):
            assert count_product_after_click == 1