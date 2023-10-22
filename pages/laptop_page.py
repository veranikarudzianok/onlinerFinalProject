import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utulites.logger import Logger


class LaptopPage(Base):

    # Locators
    trash_button = '//span[@class="compare-button__icon compare-button__icon_trash"]'
    clear_comparison_button = '//a[contains(text(), "Очистить список сравнения")]'
    add_to_comparison = '// span[@class ="catalog-masthead-controls__text helpers_hide_tablet"]'
    add_to_cart_button = '//div[1][@class="offers-list__control offers-list__control_default helpers_hide_tablet"]//a[2][contains(text(), "В корзину")]'
    go_to_cart_button = '//a[@class="button-style button-style_another button-style_base-alter product-recommended__button"]'

    # Other data
    comparison = 'Добавить к сравнению'

    # Getters
    def get_trash_button(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.trash_button)))

    def get_clear_comparison_button(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.clear_comparison_button)))

    def get_add_to_comparison(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.add_to_comparison)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_go_to_cart_button(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.go_to_cart_button)))

    # Actions
    def click_trash_button(self):
        self.get_trash_button().click()
        print('Trash button clicked')

    def click_clear_comparison_button(self):
        self.get_clear_comparison_button().click()
        print('Clear comparison button clicked')

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print('Add to cart button clicked')

    def click_go_to_cart_button(self):
        self.get_go_to_cart_button().click()
        print('Go to cart button clicked')

    # Methods
    def move_to_trash(self):
        with allure.step("Move to trash"):
            Logger.add_start_step(method="move_to_trash")
            self.click_trash_button()
            Logger.add_end_step(url=self.driver_g.current_url, method="move_to_trash")

    def clear_comparison(self):
        with allure.step("Clear comparison"):
            Logger.add_start_step(method="clear_comparison")
            self.click_clear_comparison_button()
            self.assert_word(self.get_add_to_comparison(), self.comparison)
            print("Comparison cleared")
            Logger.add_end_step(url=self.driver_g.current_url, method="clear_comparison")

    def add_laptop_to_cart(self):
        with allure.step("Add laptop to cart"):
            Logger.add_start_step(method="add_laptop_to_cart")
            self.click_add_to_cart_button()
            Logger.add_end_step(url=self.driver_g.current_url, method="add_laptop_to_cart")

    def go_to_cart(self):
        with allure.step("Go to cart"):
            Logger.add_start_step(method="go_to_cart")
            self.click_go_to_cart_button()
            Logger.add_end_step(url=self.driver_g.current_url, method="go_to_cart")