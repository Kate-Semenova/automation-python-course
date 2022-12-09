from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory


class Component(PageFactory):
    def __init__(self, element):
        self.driver = element

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def click(self):
        return self.driver.click()


class ProductInCartComponent(Component):
    locators = {
        "pr_name": (By.XPATH, "//td[2]"),
        "pr_price": (By.XPATH, "//td[3]"),
        "delete": (By.XPATH, "//*[contains(@onclick, 'deleteItem')]")
    }


class ProductComponent(Component):
    locators = {
        "pr_price": (By.XPATH, "//h5"),  # (By.TAG_NAME, "h5"), {KeyError} ???
        "pr_name": (By.XPATH, "//h4")  # (By.CLASS_NAME, 'card-title'),
    }
