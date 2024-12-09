from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".add-to-cart-btn")

    def add_product_to_cart(self, product_name):
        """Добавить товар в корзину по имени."""
        product_locator = (By.XPATH, f"//div[text()='{product_name}']/..//button[@class='add-to-cart-btn']")
        self.click_element(product_locator)
