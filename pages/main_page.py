from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utulites.logger import Logger
import allure


class MainPage(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    main_page_link_top_logo = '//div[@class="b-top-logo"]'
    open_catalog_button = '//*[@id="container"]/div/div/header/div[2]/div/nav/ul[1]/li[1]/a[2]/span'
    open_news_button = '//*[@id="container"]/div/div/header/div[2]/div/nav/ul[1]/li[2]/a/span'
    open_auto_flea_market_button = '//*[@id="container"]/div/div/header/div[2]/div/nav/ul[1]/li[3]/a/span'
    open_houses_and_apartments_button = '//*[@id="container"]/div/div/header/div[2]/div/nav/ul[1]/li[4]/a'
    open_services_button = '//*[@id="container"]/div/div/header/div[2]/div/nav/ul[1]/li[5]/a/span'
    open_flea_market_button = '//*[@id="container"]/div/div/header/div[2]/div/nav/ul[1]/li[6]/a/span'
    open_forum_button = '//*[@id="container"]/div/div/header/div[2]/div/nav/ul[1]/li[7]/a/span'

    # Other data
    url = 'https://www.onliner.by/'

    # Getters
    def get_main_page_link_top_logo(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self. main_page_link_top_logo)))

    def get_open_catalog_button(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.open_catalog_button)))

    def get_open_news_button(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.open_news_button)))

    def get_open_auto_flea_market_button(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.open_auto_flea_market_button)))

    def get_open_houses_and_apartments_button(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.open_houses_and_apartments_button)))

    def get_open_services_button(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.open_services_button)))

    def get_open_flea_market_button(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.open_flea_market_button)))

    def get_open_forum_button(self):
        return WebDriverWait(self.driver_g, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.open_forum_button)))

    # Actions
    def click_main_page_link_top_logo(self):
        self.get_main_page_link_top_logo().click()
        print('Click top logo')

    def click_open_catalog_button(self):
        self.get_open_catalog_button().click()
        print('Open Catalog page')

    def click_open_news_button(self):
        self.get_open_news_button().click()
        print('Open News page')

    def click_open_auto_flea_market_button(self):
        self.get_open_auto_flea_market_button().click()
        print('Open Auto flea page')

    def click_open_houses_and_apartments_button(self):
        self.get_open_houses_and_apartments_button().click()
        print('Open Houses and apartments page')

    def click_open_services_button(self):
        self.get_open_services_button().click()
        print('Open Services page')

    def click_open_flea_market_button(self):
        self.get_open_flea_market_button().click()
        print('Open Flea market page')

    def click_open_forum_button(self):
        self.get_open_forum_button().click()
        print('Open Forum page')

    # Methods
    def open_website(self):
        with allure.step("Open website"):
            Logger.add_start_step(method="open_website")
            self.driver_g.get(self.url)
            self.driver_g.maximize_window()
            print('Open website')
            self.assert_current_url(self.url)
            Logger.add_end_step(url=self.driver_g.current_url, method="open_website")

    def refresh_via_top_logo(self):
        with allure.step("Click top logo"):
            Logger.add_start_step(method="refresh_via_top_logo")
            self.click_main_page_link_top_logo()
            self.assert_current_url("https://www.onliner.by/")
            Logger.add_end_step(url=self.driver_g.current_url, method="refresh_via_top_logo")

    def open_news(self):
        with allure.step("Open news page"):
            Logger.add_start_step(method="open_news")
            self.click_open_news_button()
            self.assert_current_url("https://www.onliner.by/")
            Logger.add_end_step(url=self.driver_g.current_url, method="open_news")

    def open_auto_flea_market(self):
        with allure.step("Open Auto flea page"):
            Logger.add_start_step(method="open_auto_flea_market")
            self.click_open_auto_flea_market_button()
            self.assert_current_url("https://ab.onliner.by/")
            self.driver_g.back()
            Logger.add_end_step(url=self.driver_g.current_url, method="open_auto_flea_market")

    def open_houses_and_apartments(self):
        with allure.step("Open Houses and apartments page"):
            Logger.add_start_step(method="open_houses_and_apartments")
            self.click_open_houses_and_apartments_button()
            self.assert_current_url("https://r.onliner.by/pk/")
            self.driver_g.back()
            Logger.add_end_step(url=self.driver_g.current_url, method="open_houses_and_apartments")

    def open_services(self):
        with allure.step("Open Services page"):
            Logger.add_start_step(method="open_services")
            self.click_open_services_button()
            self.assert_current_url("https://s.onliner.by/tasks")
            self.driver_g.back()
            Logger.add_end_step(url=self.driver_g.current_url, method="open_services")

    def open_flea_market(self):
        with allure.step("Open Flea market page"):
            Logger.add_start_step(method="open_flea_market")
            self.click_open_flea_market_button()
            self.assert_current_url("https://baraholka.onliner.by/")
            self.driver_g.back()
            Logger.add_end_step(url=self.driver_g.current_url, method="open_flea_market")

    def open_forum(self):
        with allure.step("Open Forum page"):
            Logger.add_start_step(method="open_forum")
            self.click_open_forum_button()
            self.assert_current_url("https://forum.onliner.by/")
            self.driver_g.back()
            Logger.add_end_step(url=self.driver_g.current_url, method="open_forum")

    def open_catalog(self):
        with allure.step("Open Catalog page"):
            Logger.add_start_step(method="open_catalog")
            self.click_open_catalog_button()
            self.assert_current_url("https://catalog.onliner.by/")
            Logger.add_end_step(url=self.driver_g.current_url, method="open_catalog")