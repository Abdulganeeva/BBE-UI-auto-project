import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://demo.yookassa.ru/'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def click(self, locator, time=10):
        element = self.find_element(locator, time)
        element.click()

    def hover(self, locator):
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def open_page(self, url=''):
        self.driver.get(self.base_url + url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def refresh(self):
        self.driver.refresh()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(("tag name", "body"))
        )

    def page_tittle(self, page_name):
        page_title = self.driver.title
        if page_title == page_name:
            pass
        else:
            pytest.fail(f"Страница != {page_name}")

    def clear(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))
        self.find(locator).clear()
        time.sleep(1)

    def check_placeholder(self, locator, placeholder_text):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        placeholder = self.find(locator).get_attribute("placeholder")
        if placeholder == placeholder_text:
            pass
        else:
            pytest.fail(f"Плейсхолдер не соотвествует макету")