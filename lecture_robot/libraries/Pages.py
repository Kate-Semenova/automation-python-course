from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory

from lecture_robot.libraries.Components import ProductInCartComponent, ProductComponent


class BasePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    locators = {
        "login_button": (By.ID, 'login2'),
        "form_login_button": (By.XPATH, "//button[@onclick='logIn()']"),
        "username_input": (By.ID, "loginusername"),
        "password_input": (By.ID, "loginpassword"),
        "welcome_user": (By.ID, 'nameofuser'),
        "logout_button": (By.ID, 'logout2'),
        "monitors_menu": (By.XPATH, "//a[contains(@onclick,'monitor')]"),
        "products_list": (By.XPATH, "//*[@id='tbodyid']")
    }

    def get_list_of_products(self):
        return list(map(lambda x: ProductComponent(x),
                        self.driver.find_elements(By.XPATH, "//*[@id='tbodyid']//div[contains(@class, 'card h-100')]")))


class ProductPage(BasePage):
    locators = {
        "pr_name": (By.XPATH, "//*[@class='name']"),
        "pr_price": (By.XPATH, "//*[@class='price-container']"),
        "add_to_cart_button": (By.XPATH, "//a[contains(@onclick, 'addToCart')]"),
        "cart_link": (By.XPATH, "//*[contains(@onclick, 'showcart') or @href='cart.html']")
    }


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_products(self):
        return list(map(lambda x: ProductInCartComponent(x),
                        self.driver.find_element(By.ID, "tbodyid").find_elements(By.CLASS_NAME, "success")))
