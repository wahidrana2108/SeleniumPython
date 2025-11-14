from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

# locating using index
# user = driver.find_element(By.XPATH, value="//input[@type='text' and @placeholder='Username' or @name='user-name']")
user = driver.find_element(By.CSS_SELECTOR, value="form > div > input[type='text']")
userpass = driver.find_element(By.XPATH, value="//input[@type='password'  and @placeholder='Password' or @name='password']")
button = driver.find_element(By.XPATH, value="//input[@type='submit' and @name='login-button' and @value='Login' or @value='click here']")

user.send_keys("standard_user")
userpass.send_keys("secret_sauce")
button.click()
time.sleep(2)

# finding product using LINKTEXT
# product = driver.find_element(By.LINK_TEXT, value="Sauce Labs Bolt T-Shirt")
# product.click()


# finding product using partial LINKTEXT
# product = driver.find_element(By.PARTIAL_LINK_TEXT, value="T-Shirt (Red)")
# product.click()


# finding product using partial TagName
# tag1 = driver.find_element(By.TAG_NAME, value="button")
# tag1.click()

# finding product using partial ClassName
# classSelector = driver.find_element(By.CLASS_NAME, value="inventory_item_name ")
# classSelector.click()

# finding product using partial CSS_Selector class
# classSelector = driver.find_element(By.CSS_SELECTOR, value=".inventory_item_name ")
# classSelector.click()


# finding product using partial ID
classSelector = driver.find_element(By.CSS_SELECTOR, value="#add-to-cart-sauce-labs-backpack ")
classSelector.click()

time.sleep(5)
driver.close()