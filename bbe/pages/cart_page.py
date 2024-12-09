from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bbe.pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def delete_product_locator(self):
        return By.CSS_SELECTOR, 'button.button.js-item-delete'

    def empty_cart_locator(self):
        return By.CSS_SELECTOR, 'div.js-cart-empty'

    def plus_locator(self):
        return By.XPATH, "//span[contains(@class, 'icon') and contains(@class, 'icon-plus')]"

    def minus_locator(self):
        return By.XPATH, "//span[contains(@class, 'icon') and contains(@class, 'icon-minus')]"

    def count_product_locator(self):
        return By.XPATH, "//input[contains(@class, 'counter-input')]"

    def make_order_locator(self):
        return By.XPATH, "//button[text()='Оформить заказ']"

    def coupon_element_locator(self):
        return By.NAME, "cart[coupon]"

    def delete_product_from_cart(self):
        self.click(self.delete_product_locator())

    def find_empty_cart_element(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.empty_cart_locator()))
        return self.find(self.empty_cart_locator())

    def click_plus(self):
        self.click(self.plus_locator())

    def click_minus(self):
        self.click(self.minus_locator())

    def get_count_product(self):
        count_element = self.find(self.count_product_locator())
        return int(count_element.get_attribute('value'))

    def click_make_order(self):
        self.click(self.make_order_locator())

    def check_coupon_place_holder(self):
        self.check_placeholder(self.coupon_element_locator(), "Промокод")