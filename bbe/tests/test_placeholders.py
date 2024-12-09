import allure
import pytest

from bbe.pages.start_page import StartPage


@pytest.mark.usefixtures("init_driver")
class TestPlaceholders:
    @allure.title("Тест на соотвествие плейсхолдера поля Промокод макету")
    def test_check_coupon_placeholder(self, cart_page):

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

        with allure.step('Проверка плейсхолдера поля Промокод'):
            cart_page.check_coupon_place_holder()