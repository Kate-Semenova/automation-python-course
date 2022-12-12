import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages import HomePage, ProductPage, CartPage
from my_expected_conditions import wait_for_number_of_elements_more_than_0, wait_for_number_of_elements_is_0


class MySteps:
    ROBOT_LIBRARY_SCOPE = 'SUITE'

    DATA_CASH = {}

    url = 'https://www.demoblaze.com/'

    def __init__(self):
        self.wait = None
        self.chromedriver = None
        self.homepage = None
        self.productpage = None
        self.cartpage = None

    def start_webdriver(self):
        self.chromedriver = webdriver.Chrome()
        self.chromedriver.maximize_window()
        self.wait = WebDriverWait(self.chromedriver, 5)
        self.homepage = HomePage(self.chromedriver)
        self.productpage = ProductPage(self.chromedriver)
        self.cartpage = CartPage(self.chromedriver)

        self.chromedriver.get(self.url)

    def close_webdriver(self):
        self.chromedriver.close()

    def click_login_button(self):
        self.homepage.login_button.click()

    def login_button_is_presented(self):
        return self.wait.until(expected_conditions.visibility_of(self.homepage.form_login_button))

    def set_up_login_and_password(self, login, password):
        self.homepage.username_input.send_keys(login)
        self.homepage.password_input.send_keys(password)
        self.click_form_login_button()

    def log_out_button_is_presented(self):
        return self.wait.until(expected_conditions.visibility_of(
            self.homepage.logout_button))

    def welcome_message_is_presented(self, username):
        return username in self.homepage.welcome_user.text

    def click_form_login_button(self):
        self.homepage.form_login_button.click()

    def click_on_monitors_category(self):
        self.homepage.monitors_menu.click()
        time.sleep(1)  # the only quick way to wait until correct category is opened

    def click_on_the_product_with_the_highest_price_on_the_page(self):
        self.wait.until(wait_for_number_of_elements_more_than_0(self.homepage.get_list_of_products))
        products = self.homepage.get_list_of_products()
        products_prices = {}
        list(map(lambda x:
                 products_prices.setdefault(x,
                                            list(map(int, re.findall(r'\d+', x.find_element(By.TAG_NAME, "h5").text)))[
                                                0])
                 , products))
        highest_price_product = max(products_prices, key=products_prices.get)

        self.DATA_CASH.setdefault("PRODUCT_PRICE", products_prices[highest_price_product])
        self.DATA_CASH.setdefault("PRODUCT_NAME", highest_price_product.find_element(By.CLASS_NAME, 'card-title').text)

        highest_price_product.click()

    def get_highest_price_product_name(self):
        return self.DATA_CASH["PRODUCT_NAME"]

    def get_highest_price_product_price(self):
        return self.DATA_CASH["PRODUCT_PRICE"]

    def products_page_with_is_open(self, name, price):
        return self.productpage.pr_name.is_displayed() and \
               self.productpage.pr_price.is_displayed() and \
               self.productpage.pr_name.text == name and \
               list(map(int, re.findall(r'\d+', self.productpage.pr_price.text)))[0] == price

    def click_on_add_to_cart_button(self):
        self.productpage.add_to_cart_button.click()
        self.wait.until(expected_conditions.alert_is_present())
        self.chromedriver.switch_to.alert.accept()

    def click_on_cart_button(self):
        self.productpage.cart_link.click()

    def product_is_successfully_added_to_cart(self):
        self.wait.until(wait_for_number_of_elements_more_than_0(self.cartpage.get_products))
        return len(self.cartpage.get_products()) > 0

    def get_product_name_text(self):
        return self.cartpage.get_products()[0].pr_name.text

    def get_product_price_text(self):
        return int(self.cartpage.get_products()[0].pr_price.text)

    def clean_cart(self):
        self.click_on_cart_button()
        self.wait.until(wait_for_number_of_elements_more_than_0(self.cartpage.get_products))
        self.cartpage.get_products()[0].delete.click()
        self.wait.until(wait_for_number_of_elements_is_0(self.cartpage.get_products))
