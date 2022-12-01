from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.saucedemo.com/"

chrome_driver = webdriver.Chrome()
chrome_driver.get(url)
chrome_driver.find_element(By.ID, "user-name").send_keys("standard_user")
chrome_driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("secret_sauce")
chrome_driver.find_element(By.XPATH, "//input[contains(@class,'submit-button')]").click()

current_url = chrome_driver.current_url

assert current_url == "https://www.saucedemo.com/inventory.html"

chrome_driver.close()
