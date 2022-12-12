from selenium.common import StaleElementReferenceException


class wait_for_number_of_elements_more_than_0(object):
    def __init__(self, elements):
        self.elements = elements

    def __call__(self, driver):
        try:
            return len(self.elements()) > 0
        except StaleElementReferenceException:
            return False


class wait_for_number_of_elements_is_0(object):
    def __init__(self, elements):
        self.elements = elements

    def __call__(self, driver):
        try:
            return len(self.elements()) == 0
        except StaleElementReferenceException:
            return False
