import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utulites.logger import Logger


class CartPage(Base):
    # Locators
    registration_button = '//a[@class="button-style button-style_small cart-form__button button-style_primary"]'

    # Getters
    def get_registration_button(self):
        return WebDriverWait(self.driver_g, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.registration_button)))

    # Actions
    def click_registration_button(self):
        self.get_registration_button().click()
        print('Registration button clicked')

    # Methods
    def move_to_registration(self):
        with allure.step("Move to registration"):
            Logger.add_start_step(method="move_to_registration")
            self.click_registration_button()
            Logger.add_end_step(url=self.driver_g.current_url, method="move_to_registration")