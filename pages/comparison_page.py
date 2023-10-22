import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utulites.logger import Logger

product1_name_on_comparison_page_to_text = '1'
product2_name_on_comparison_page_to_text = '2'


class ComparisonPage(Base):

    # Locators
    amount_of_offers_first_product_comparison = '//*[@id="product-table"]/tbody[2]/tr/th[3]/div/div//a[@class="button button_orange"]'
    amount_of_offers_second_product_comparison = '//*[@id="product-table"]/tbody[2]/tr/th[4]/div/div//a[@class="button button_orange"]'
    product1_name_on_comparison_page = '//*[@id="product-table"]/tbody[2]/tr/th[3]/div/div/a/span'
    product2_name_on_comparison_page = '//*[@id="product-table"]/tbody[2]/tr/th[4]/div/div/a/span'

    # Getters
    def get_product1_name_on_comparison_page(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product1_name_on_comparison_page)))

    def get_product2_name_on_comparison_page(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product2_name_on_comparison_page)))

    def get_amount_of_offers_first_product_comparison(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.amount_of_offers_first_product_comparison)))

    def get_amount_of_offers_second_product_comparison(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.amount_of_offers_second_product_comparison)))

    # Actions
    def click_amount_of_offers_first_product_comparison(self):
        self.get_amount_of_offers_first_product_comparison().click()

    def click_amount_of_offers_second_product_comparison(self):
        self.get_amount_of_offers_second_product_comparison().click()

    # Methods

    def save_product1_name_on_comparison_page(self):
        with allure.step("Save first product name"):
            Logger.add_start_step(method="save_product1_name_on_comparison_page")
            global product1_name_on_comparison_page_to_text
            name_of_product1_on_comparison_page = self.get_product1_name_on_comparison_page()
            product1_name_on_comparison_page_to_text = name_of_product1_on_comparison_page.text
            print(product1_name_on_comparison_page_to_text)
            Logger.add_end_step(url=self.driver_g.current_url, method="save_product1_name_on_comparison_page")
            return product1_name_on_comparison_page_to_text

    def save_product2_name_on_comparison_page(self):
        with allure.step("Save second product name"):
            Logger.add_start_step(method="save_product2_name_on_comparison_page")
            global product2_name_on_comparison_page_to_text
            name_of_product2_on_comparison_page = self.get_product2_name_on_comparison_page()
            product2_name_on_comparison_page_to_text = name_of_product2_on_comparison_page.text
            print(product2_name_on_comparison_page_to_text)
            Logger.add_end_step(url=self.driver_g.current_url, method="save_product2_name_on_comparison_page")
            return product2_name_on_comparison_page_to_text

    def select_offer(self):
        with allure.step("Select offer"):
            Logger.add_start_step(method="select_offer")
            self.click_amount_of_offers_second_product_comparison()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_offer")