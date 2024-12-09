from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def phone_locator(self):
        return By.ID, "client_phone"

    def address_locator(self):
        return By.ID, "shipping_address_full_locality_name"

    def address_error_locator(self):
        return (By.XPATH, "//input[@id='shipping_address_full_locality_name']"
                          "/following-sibling::div[@class='co-input-notice co-notice--danger']")

    def name_locator(self):
        return By.ID, "client_name"

    def name_error_locator(self):
        return By.XPATH, ("//input[@id='client_name']"
                          "/following-sibling::div[@class='co-input-notice co-notice--danger']")

    def accept_order_button(self):
        return By.ID, "create_order"

    def make_phone(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.phone_locator()))
        self.find(self.phone_locator()).clear()
        self.find(self.phone_locator()).send_keys("1234567890")

    def make_address(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.address_locator()))
        self.find(self.address_locator()).clear()
        self.find(self.address_locator()).send_keys("г Воронеж, Воронежская обл.")

    def make_name(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.name_locator()))
        self.find(self.name_locator()).clear()
        self.find(self.name_locator()).send_keys("Ксения")

    def click_order_button(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.accept_order_button()))
        self.click(self.accept_order_button())

    def clear_name(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.name_locator()))
        self.find(self.name_locator()).clear()

    def clear_address(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.address_locator()))
        self.find(self.address_locator()).clear()

    def find_address_error(self):
        return self.find(self.address_error_locator())

    def find_name_error(self):
        return self.find(self.name_error_locator())