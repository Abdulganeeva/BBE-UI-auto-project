import allure
import pytest

from bbe.pages.start_page import StartPage


@pytest.mark.usefixtures("init_driver")
class TestDeleteFromCart:
    @allure.title("Тест на удаление товара из корзины")
    def test_delete_from_cart(self, cart_page):

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

        with allure.step('Удаление товара из корзины'):
            cart_page.delete_product_from_cart()

        with allure.step('Проверка, что текст на странице изменился'):
            empty_cart_element = cart_page.find_empty_cart_element()
            assert empty_cart_element.text == "Ваша корзина пуста"