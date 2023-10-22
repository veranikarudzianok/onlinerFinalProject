import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utulites.logger import Logger


class OrderPage(Base):

    # Locators
    street = '//*[@id="container"]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[3]/div/div[4]/div[1]/div[2]/div/div/div/div/div/input'
    house = '//*[@id="container"]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[3]/div/div[4]/div[3]/div[2]/div/input'
    liter = '//*[@id="container"]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[3]/div/div[4]/div[4]/div[2]/div/input'
    entrance = '//*[@id="container"]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[3]/div/div[4]/div[6]/div[2]/div/input'
    floor = '//*[@id="container"]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[3]/div/div[4]/div[7]/div[2]/div/input'
    apartment = '//*[@id="container"]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[3]/div/div[4]/div[8]/div[2]/div/input'
    comment = '//textarea[@placeholder="Укажите дополнительные детали"]'
    first_name = '//*[@id="container"]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[3]/div/div[9]/div[1]/div[2]/div/input'
    last_name = '//*[@id="container"]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[3]/div/div[9]/div[2]/div[2]/div/input'
    email = '//*[@id="container"]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[3]/div/div[10]/div[1]/div[2]/div/input'
    phone = '//*[@id="container"]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[3]/div/div[10]/div[2]/div[3]/div[1]/div/div[1]/input'
    go_to_payment_button = '//button[@class="button-style button-style_primary button-style_base cart-form__button cart-form__button_responsive"]'

    # Getters
    def get_street(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.street)))

    def get_house(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.house)))

    def get_liter(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.liter)))

    def get_entrance(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.entrance)))

    def get_floor(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.floor)))

    def get_apartment(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.apartment)))

    def get_comment(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.comment)))

    def get_first_name(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_email(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.email)))

    def get_phone(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.phone)))

    def get_go_to_payment_button(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.go_to_payment_button)))

    # Actions
    def input_street(self,):
        self.get_street().send_keys("Street")
        print('Input street')

    def input_house(self,):
        self.get_house().send_keys("7")
        print('Input House')

    def input_liter(self,):
        self.get_liter().send_keys("1A")
        print('Input Liter')

    def input_entrance(self,):
        self.get_entrance().send_keys("1")
        print('Input entrance')

    def input_floor(self,):
        self.get_floor().send_keys("4")
        print('Input floor')

    def input_apartment(self,):
        self.get_apartment().send_keys("20")
        print('Input Apartment')

    def input_comment(self,):
        self.get_comment().send_keys("Comment")
        print('Input Comment')

    def input_first_name(self,):
        self.get_first_name().send_keys("First Name")
        print('Input First Name')

    def input_last_name(self,):
        self.get_last_name().send_keys("Last Name")
        print('Input Last Name')

    def input_email(self,):
        self.get_email().send_keys("veranika.rudzianok@gmail.com")
        print('Input email')

    def input_phone(self,):
        self.get_phone().send_keys("256345742")
        print('Input phone')

    def click_go_to_payment_button(self):
        self.get_go_to_payment_button().click()
        print('Go to payment button clicked')

    # Methods
    def enter_information(self):
        with allure.step("Enter information"):
            Logger.add_start_step(method="enter_information")
            self.input_street()
            self.input_house()
            self.input_liter()
            self.input_entrance()
            self.input_floor()
            self.input_apartment()
            self.input_comment()
            self.input_first_name()
            self.input_last_name()
            self.input_email()
            self.input_phone()
            self.click_go_to_payment_button()
            Logger.add_end_step(url=self.driver_g.current_url, method="enter_information")

    def finish(self):
        with allure.step("Finish screenshot"):
            Logger.add_start_step(method="finish")
            self.make_screenshot()
            Logger.add_end_step(url=self.driver_g.current_url, method="finish")