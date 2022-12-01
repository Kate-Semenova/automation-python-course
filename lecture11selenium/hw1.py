from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "login_input": ('id', 'user-name'),
        "password_input": ('css', "input[placeholder='Password']"),
        "sign_button": ('xpath', "//input[contains(@class,'submit-button')]")
    }

    def enter_login(self, login):
        return self.login_input.set_text(login)

    def enter_password(self, password):
        return self.password_input.set_text(password)

    def submit_login_form(self):
        return self.sign_button.click_button()

    def log_in(self, login, password):
        self.enter_login(login)
        self.enter_password(password)
        self.submit_login_form()


def test_login():
    url = "https://www.saucedemo.com/"
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(url)
    login_page = LoginPage(chrome_driver)
    login_page.log_in('standard_user', 'secret_sauce')



    assert chrome_driver.current_url == "https://www.saucedemo.com/inventory.html"

    chrome_driver.close()


""" ЗАДАНИЕ
Есть сайт https://www.saucedemo.com/
"""
"""
Необходимо написать скрипт, в котором:
1. С помощью методов Selenium WebDriver открываем наш сайт (https://www.saucedemo.com/)
2. С помощью методов Selenium WebDriver в поле Username вводим корректное имя (см. ниже)
3. С помощью методов Selenium WebDriver в поле Password вводим корректный пароль (см. ниже)
4. С помощью методов Selenium WebDriver кликаем по кнопке Login (см. ниже)
5. С помощью методов Selenium WebDriver получаем текущий URL (после авторизации)
6. Через Assert сравниваем полученный URL с заданным (например, https://www.saucedemo.com/inventory.html)

* Важное условие - необходимо использовать как минимум 2 разных метода поиска по типу локаторов
(например, для поля имени используем поиск по DOM - предположим, используя By.ID,
а для поля пароля поиск по XPath - By.XPATH)

* На главной странице этого сайта указаны корректные связки Username-Password, например, эти:
standard_user
secret_sauce

### Установка Selenium и WebDriver
Напоминаю, что установка пакета селениума осуществляется с помощью команды pip install selenium.
Помимо прочего, для локального запуска, необходимо скачать и поставить себе Selenium WebDriver
(для браузеров Google Chrome, например, доступно по ссылке - https://chromedriver.chromium.org/downloads).
Не забываем, что необходимо ставить версию, соответствующую мажорной версии вашего браузера.
Также не забываем, что путь до вашего веб-драйвера надо указать в Переменных средах (подробнее тут -
https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver)

### РЕВЬЮ
В качестве ревьюера указывайте меня, пожалуйста (@VAlexandrov911)
"""
