import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utulites.logger import Logger

product1_name_on_catalog_page_to_text = '1'
product2_name_on_catalog_page_to_text = '2'

class CatalogPage(Base):

    # Locators
    catalog_navigation_title = '//div[@class="catalog-navigation__title"]'
    # navigation_link = '//span[@class ="b-main-navigation__text" and text()[contains(., "{}")]]'
    computers_and_networks_link = '//li[@data-id="2"]'
    laptops_computers_monitors_link = '//div[@class ="catalog-navigation-list__aside-title" and text()[contains(., "{}")]]'
    laptops_link = '//a[@href="https://catalog.onliner.by/notebook"]'
    laptops_title = '//h1[@class="schema-header__title js-schema-header_title"]'
    city_confirmation_button = '//span[contains(text(), "Да, верно")]'
    city_link = '//*[@id="schema-filter"]/div[4]/div/div/div/a'
    all_producers_field = '//*[@id="schema-filter"]/div[5]/div[4]/div[2]/div[1]/div'
    text_number_of_producers = '//*[@id="schema-filter"]/div[5]/div[4]/div[2]/div[1]/div/span[1]'
    number_of_producers = '//div[@class="schema-filter-popover schema-filter-popover_visible"]/div/div[2]/div'
    producer_checkbox = '//*[@class="schema-filter__checkbox-text" and text()[contains(.,"{}")]]'
    producer_tag_box = '//div[@title="Производитель"]//span[@class="schema-tags__text"]'
    max_price_field = '//input[@placeholder="до"]'
    max_price_tag_box = '//*[@id="schema-tags"]/div[2]/span'
    purpose_checkbox = '//*[@id="schema-filter"]/div[5]/div[8]/div[3]/ul/li[1]/label/span[2]'
    purpose_tag_box = '//div[@title="Подобрать в один клик"]//span[@class="schema-tags__text"]'
    screen_size_option = '//div[@class="schema-filter__group"]/div[2]//option[contains(text(), "15.0")]'
    screen_size_tag_box = '//div[@title="Диагональ экрана"]//span[@class="schema-tags__text"]'
    super_button = '//span[@class="button-style button-style_another button-style_base schema-product__tutorial-button"]'
    first_product_checkbox = '//*[@id="schema-products"]/div[2]/div/div[1]/div[1]/div'
    second_product_checkbox = '//*[@id="schema-products"]/div[3]/div/div[1]/div[1]/div'
    product1_name_on_catalog_page = '//*[@id="schema-products"]/div[2]/div/div[3]/div[2]/div[1]/a/span'
    product2_name_on_catalog_page = '//*[@id="schema-products"]/div[3]/div/div[3]/div[2]/div[1]/a/span'
    order_link = '//a[@class="schema-order__link"]'
    order_base = '//a[@class="schema-order__link"]/span[2]'
    order_option = '//span[@data-bind="text: $root.items[type].text" and text()[contains(., "{}")]]'
    compare_button = '//a[@class="compare-button__sub compare-button__sub_main"]'

    # Other data
    url = 'https://catalog.onliner.by/'
    catalog_navigation_title_text = 'Каталог'
    laptops_computers_monitors_link_title = ' Ноутбуки, компьютеры, мониторы '
    producer_name = 'Apple'
    max_price_value = '7 000'
    purpose = 'для работы'
    laptops = 'Ноутбуки'
    city = 'Минск'
    default_order_base = 'популярные'
    order_option_text = 'Дешевые'

    # Formats
    laptops_computers_monitors_link_format = laptops_computers_monitors_link.format(laptops_computers_monitors_link_title)
    producer_checkbox_format = producer_checkbox.format(producer_name)
    purpose_checkbox_format = purpose_checkbox.format(purpose)
    order_option_format = order_option.format(order_option_text)

    # Getters
    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.name_of_product1_catalog_to_text = None

    def get_catalog_navigation_title(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.catalog_navigation_title)))

    def get_computers_and_networks_link(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.computers_and_networks_link)))

    def get_laptops_computers_monitors_link(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.laptops_computers_monitors_link_format)))

    def get_laptops_link(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.laptops_link)))

    def get_laptops_title(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.laptops_title)))

    def get_city_confirmation_button(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.city_confirmation_button)))

    def get_city_link(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.city_link)))

    def get_all_producers_field(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.all_producers_field)))

    def get_text_number_of_producers(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.text_number_of_producers)))

    def get_number_of_producers(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.number_of_producers)))

    def get_producer_checkbox(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.producer_checkbox_format)))

    def get_max_price_field(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.max_price_field)))

    def get_purpose_checkbox(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.purpose_checkbox_format)))

    def get_screen_size_option(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.screen_size_option)))

    def get_producer_tag_box(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.producer_tag_box)))

    def get_max_price_tag_box(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.max_price_tag_box)))

    def get_purpose_tag_box(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.purpose_tag_box)))

    def get_screen_size_tag_box(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.screen_size_tag_box)))

    def get_super_button(self):
        return WebDriverWait(self.driver_g,10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.super_button)))

    def get_first_product_checkbox(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.first_product_checkbox)))

    def get_second_product_checkbox(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.second_product_checkbox)))

    def get_order_link(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.order_link)))

    def get_order_base(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.order_base)))

    def get_order_option(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.order_option_format)))

    def get_compare_button(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.compare_button)))

    def get_product1_name_on_catalog_page(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product1_name_on_catalog_page)))

    def get_product2_name_on_catalog_page(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product2_name_on_catalog_page)))

    # Actions
    def click_computers_and_networks_link(self):
        self.get_computers_and_networks_link().click()
        print('Open Computers and networks')

    def click_laptops_computers_monitors_link(self):
        self.get_laptops_computers_monitors_link().click()
        print('Open Laptops, computers, monitors')

    def click_laptops_link(self):
        self.get_laptops_link().click()
        print('Open Laptops')

    def click_city_confirmation_button(self):
        self.get_city_confirmation_button().click()
        print('City confirmed')

    def click_all_producers_field(self):
        self.get_all_producers_field().click()
        print('Open list of producers')

    def click_apple_producer_checkbox(self):
        self.get_producer_checkbox().click()
        print('Select Apple producer')

    def click_purpose_checkbox(self):
        self.get_purpose_checkbox().click()
        print('Select purpose')

    def click_screen_size_option(self):
        self.get_screen_size_option().click()
        print('Select screen size')

    def click_super_button(self):
        self.get_super_button().click()
        print('Close pop up')

    def click_first_product_checkbox(self):
        self.get_first_product_checkbox().click()
        print('Add product 1 to comparison')

    def click_second_product_checkbox(self):
        self.get_second_product_checkbox().click()
        print('Add product 2 to comparison')

    def click_order_link(self):
        self.get_order_link().click()
        print('Open orders')

    def click_order_base(self):
        self.get_order_base().click()
        print('Select order')

    def click_order_option(self):
        self.get_order_option().click()
        print('Select order')

    def click_compare_products_button(self):
        self.get_compare_button().click()
        print('Go to comparison page')

    # Methods
    def check_catalog_navigation_title(self):
        with allure.step("Check catalog navigation title"):
            Logger.add_start_step(method="check_catalog_navigation_title")
            catalog_title = self.get_catalog_navigation_title().text
            if self.catalog_navigation_title_text in catalog_title:
                print('Catalog navigation title is correct')
            Logger.add_end_step(url=self.driver_g.current_url, method="check_catalog_navigation_title")

    def open_computers_and_networks(self):
        with allure.step("Open computers and networks"):
            Logger.add_start_step(method="open_computers_and_networks")
            self.click_computers_and_networks_link()
            Logger.add_end_step(url=self.driver_g.current_url, method="open_computers_and_networks")

    def open_laptops_computers_monitors(self):
        with allure.step("Open laptops, computers, monitors"):
            Logger.add_start_step(method="open_laptops_computers_monitors")
            self.click_laptops_computers_monitors_link()
            Logger.add_end_step(url=self.driver_g.current_url, method="open_laptops_computers_monitors")

    def open_laptops(self):
        with allure.step("Open laptops"):
            Logger.add_start_step(method="open_laptops")
            self.click_laptops_link()
            Logger.add_end_step(url=self.driver_g.current_url, method="open_laptops")

    def check_laptops_title(self):
        with allure.step("Check laptops title"):
            Logger.add_start_step(method="check_laptops_title")
            self.assert_word(self.get_laptops_title(), self.laptops)
            Logger.add_end_step(url=self.driver_g.current_url, method="check_laptops_title")

    def confirm_city(self):
        with allure.step("Confirm city"):
            Logger.add_start_step(method="confirm_city")
            self.click_city_confirmation_button()
            Logger.add_end_step(url=self.driver_g.current_url, method="confirm_city")

    def check_city(self):
        with allure.step("Check city"):
            Logger.add_start_step(method="check_city")
            self.assert_word(self.get_city_link(), self.city)
            print('City is correct')
            Logger.add_end_step(url=self.driver_g.current_url, method="check_city")

    def open_all_producers(self):
        with allure.step("Open all producers"):
            Logger.add_start_step(method="open_all_producers")
            self.driver_g.execute_script('window.scrollTo(0, 900)')
            time.sleep(1)
            self.click_all_producers_field()
            time.sleep(1)
            Logger.add_end_step(url=self.driver_g.current_url, method="open_all_producers")

    def select_producer(self):
        with allure.step("Select producer"):
            Logger.add_start_step(method="select_producer")
            self.click_apple_producer_checkbox()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_producer")

    def check_text_number_of_producers(self):
        with allure.step("Check text number of producers"):
            Logger.add_start_step(method="check_text_number_of_producers")
            self.driver_g.execute_script('window.scrollTo(0, 900)')
            text_number_of_producers = self.get_text_number_of_producers().text
            Logger.add_end_step(url=self.driver_g.current_url, method="check_text_number_of_producers")
            return text_number_of_producers

    def count_number_of_producers(self):
        with allure.step("Count number of producers"):
            Logger.add_start_step(method="count_number_of_producers")
            self.driver_g.execute_script('window.scrollTo(0, 0)')
            number_of_producers = self.driver_g.find_elements(By.XPATH, self.number_of_producers)
            Logger.add_end_step(url=self.driver_g.current_url, method="count_number_of_producers")
            return len(number_of_producers)

    def check_number_of_producers(self):
        with allure.step("Check number of producers"):
            Logger.add_start_step(method="check_number_of_producers")
            value_text_number_of_producers = self.check_text_number_of_producers()
            print('Text number of producers is:', value_text_number_of_producers)
            value_number_of_producers = self.count_number_of_producers()
            print('Number of producers is:', value_number_of_producers)
            assert int(value_text_number_of_producers) == int(value_number_of_producers)
            print('Number of producers is correct')
            Logger.add_end_step(url=self.driver_g.current_url, method="check_number_of_producers")

    def enter_max_price(self):
        with allure.step("Enter max price"):
            Logger.add_start_step(method="enter_max_price")
            self.driver_g.execute_script('window.scrollTo(0, 1000)')
            self.get_max_price_field().send_keys(self.max_price_value)
            Logger.add_end_step(url=self.driver_g.current_url, method="enter_max_price")

    def select_purpose(self):
        with allure.step("Select purpose"):
            Logger.add_start_step(method="select_purpose")
            self.click_purpose_checkbox()
            print('Purpose selected')
            Logger.add_end_step(url=self.driver_g.current_url, method="select_purpose")

    def select_screen_size(self):
        with allure.step("Select screen size"):
            Logger.add_start_step(method="select_screen_size")
            self.driver_g.execute_script('window.scrollTo(0, 2000)')
            self.click_screen_size_option()
            print('Screen size option selected')
            Logger.add_end_step(url=self.driver_g.current_url, method="select_screen_size")

    def check_producer(self):
        with allure.step("Check producer"):
            Logger.add_start_step(method="check_producer")
            self.driver_g.execute_script('window.scrollTo(0, 0)')
            self.assert_word(self.get_producer_tag_box(), self.producer_name)
            print('Producer is correct')
            Logger.add_end_step(url=self.driver_g.current_url, method="check_producer")

    def check_max_price(self):
        with allure.step("Check max price"):
            Logger.add_start_step(method="check_max_price")
            selected_max_price = 'до ' + str(self.max_price_value)
            self.assert_word(self.get_max_price_tag_box(), selected_max_price)
            print('Max price is correct')
            Logger.add_end_step(url=self.driver_g.current_url, method="check_max_price")

    def check_purpose(self):
        with allure.step("Check purpose"):
            Logger.add_start_step(method="check_purpose")
            self.assert_word(self.get_purpose_tag_box(), self.get_purpose_checkbox().text)
            print('Purpose is correct')
            Logger.add_end_step(url=self.driver_g.current_url, method="check_purpose")

    def check_screen_size(self):
        with allure.step("Check screen size"):
            Logger.add_start_step(method="check_screen_size")
            time.sleep(1)
            selected_size_box_option = 'до '+ str(self.get_screen_size_option().text)
            self.assert_word(self.get_screen_size_tag_box(), selected_size_box_option)
            Logger.add_end_step(url=self.driver_g.current_url, method="check_screen_size")

    def check_default_order_base(self):
        with allure.step("Check default order base"):
            Logger.add_start_step(method="check_default_order_base")
            self.assert_word(self.get_order_base(), self.default_order_base)
            Logger.add_end_step(url=self.driver_g.current_url, method="check_default_order_base")

    def select_order_option(self):
        with allure.step("Select order option"):
            Logger.add_start_step(method="select_order_option")
            time.sleep(1)
            self.click_order_link()
            self.click_order_option()
            self.assert_word(self.get_order_base(), self.order_option_text.lower())
            Logger.add_end_step(url=self.driver_g.current_url, method="select_order_option")

    def close_popover(self):
        with allure.step("Close popover"):
            Logger.add_start_step(method="close_popover")
            self.click_super_button()
            Logger.add_end_step(url=self.driver_g.current_url, method="close_popover")

    def save_product1_name_on_catalog_page(self):
        with allure.step("Save first product name"):
            Logger.add_start_step(method="save_product1_name_on_catalog_page")
            time.sleep(1)
            global product1_name_on_catalog_page_to_text
            name_of_product1_on_catalog_page = self.get_product1_name_on_catalog_page()
            product1_name_on_catalog_page_to_text = name_of_product1_on_catalog_page.text
            print(product1_name_on_catalog_page_to_text)
            Logger.add_end_step(url=self.driver_g.current_url, method="save_product1_name_on_catalog_page")
            return product1_name_on_catalog_page_to_text

    def save_product2_name_on_catalog_page(self):
        with allure.step("Save second product name"):
            Logger.add_start_step(method="save_product2_name_on_catalog_page")
            time.sleep(1)
            global product2_name_on_catalog_page_to_text
            name_of_product2_on_catalog_page = self.get_product2_name_on_catalog_page()
            product2_name_on_catalog_page_to_text = name_of_product2_on_catalog_page.text
            print(product2_name_on_catalog_page_to_text)
            Logger.add_end_step(url=self.driver_g.current_url, method="save_product2_name_on_catalog_page")
            return product2_name_on_catalog_page_to_text

    def add_first_product_to_comparison(self):
        with allure.step("Add first product to comparison"):
            Logger.add_start_step(method="add_first_product_to_comparison")
            time.sleep(3)
            self.click_first_product_checkbox()
            Logger.add_end_step(url=self.driver_g.current_url, method="add_first_product_to_comparison")

    def add_second_product_to_comparison(self):
        with allure.step("Add second product to comparison"):
            Logger.add_start_step(method="add_first_product_to_comparison")
            time.sleep(3)
            self.click_second_product_checkbox()
            Logger.add_end_step(url=self.driver_g.current_url, method="add_first_product_to_comparison")

    def open_comparison_page(self):
        with allure.step("Open comparison page"):
            Logger.add_start_step(method="open_comparison_page")
            self.click_compare_products_button()
            Logger.add_end_step(url=self.driver_g.current_url, method="open_comparison_page")