from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from base.base_class import Base
from pages.laptop_page import LaptopPage
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage, product1_name_on_catalog_page_to_text, product2_name_on_catalog_page_to_text
from pages.comparison_page import ComparisonPage, product1_name_on_comparison_page_to_text, \
    product2_name_on_comparison_page_to_text
from pages.cart_page import CartPage
from pages.order_page import OrderPage
import allure

@allure.description("Test navigation bar")
def test_navigation_bar(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\PyCharmProjects\\1\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    """Pages"""
    main_page = MainPage(driver_g)

    """Test run"""
    main_page.open_website()
    main_page.refresh_via_top_logo()
    main_page.open_news()
    main_page.open_auto_flea_market()
    main_page.open_houses_and_apartments()
    main_page.open_services()
    main_page.open_flea_market()
    main_page.open_forum()
    main_page.open_catalog()

@allure.description("Test buy filtered laptop")
def test_buy_filtered_laptop(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\PyCharmProjects\\1\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    """Pages"""
    main_page = MainPage(driver_g)
    catalog_page = CatalogPage(driver_g)
    comparison_page = ComparisonPage(driver_g)
    laptop_page = LaptopPage(driver_g)
    cart_page = CartPage(driver_g)
    order_page = OrderPage(driver_g)
    base_class = Base(driver_g)

    """Test run"""
    main_page.open_website()
    main_page.open_catalog()
    catalog_page.check_catalog_navigation_title()
    catalog_page.open_computers_and_networks()
    catalog_page.open_laptops_computers_monitors()
    catalog_page.open_laptops()
    catalog_page.close_popover()
    catalog_page.check_laptops_title()
    catalog_page.confirm_city()
    catalog_page.check_city()
    catalog_page.open_all_producers()
    catalog_page.check_number_of_producers()
    catalog_page.open_all_producers()
    catalog_page.select_producer()
    catalog_page.enter_max_price()
    catalog_page.select_purpose()
    catalog_page.select_screen_size()
    catalog_page.check_producer()
    catalog_page.check_max_price()
    catalog_page.check_purpose()
    catalog_page.check_screen_size()
    catalog_page.check_default_order_base()
    catalog_page.select_order_option()
    catalog_page.save_product1_name_on_catalog_page()
    catalog_page.save_product2_name_on_catalog_page()
    catalog_page.add_first_product_to_comparison()
    catalog_page.add_second_product_to_comparison()
    catalog_page.open_comparison_page()
    comparison_page.save_product1_name_on_comparison_page()
    comparison_page.save_product2_name_on_comparison_page()
    base_class.assert_product_names(product1_name_on_catalog_page_to_text, product1_name_on_comparison_page_to_text)
    base_class.assert_product_names(product2_name_on_catalog_page_to_text, product2_name_on_comparison_page_to_text)
    comparison_page.select_offer()
    laptop_page.move_to_trash()
    laptop_page.clear_comparison()
    laptop_page.add_laptop_to_cart()
    laptop_page.go_to_cart()
    cart_page.click_registration_button()
    order_page.enter_information()
    order_page.finish()