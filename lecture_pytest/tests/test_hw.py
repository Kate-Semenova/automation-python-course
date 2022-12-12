import pytest
from _pytest.fixtures import fixture

from lecture_robot.libraries.MySteps import MySteps
from lecture_pytest.common.constants import PASSWORD, USERNAME

step = MySteps()


def setup_module():
    step.start_webdriver()


@pytest.mark.parametrize('username, password', [(USERNAME, PASSWORD), ("katerina_new_test", PASSWORD)])
@pytest.mark.usefixtures('log_out')
def test_log_in(username, password):
    step.click_login_button()
    assert step.login_and_password_fields_are_presented()
    step.set_up_login_and_password(username, password)
    step.click_form_login_button()
    assert step.log_out_button_is_presented()
    assert step.welcome_message_is_presented(username)


def test_add_product(login_user_and_clean_cart):
    step.click_on_monitors_category()
    step.click_on_the_product_with_the_highest_price_on_the_page()
    name = step.get_highest_price_product_name()
    price = step.get_highest_price_product_price()
    assert step.products_page_with_is_open(name, price)
    step.click_on_add_to_cart_button()
    step.click_on_cart_button()
    assert step.product_is_successfully_added_to_cart()
    name_cart = step.get_product_name_text()
    price_cart = step.get_product_price_text()
    assert name_cart == name
    assert price_cart == price


def teardown_module():
    step.close_webdriver()


@fixture()
def login_user_and_clean_cart():
    step.log_in_with(USERNAME, PASSWORD)
    yield
    step.clean_cart()


@fixture()
def log_out():
    yield
    step.log_out()
