from itertools import product

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
# time.sleep(2)

# username = driver.find_element(By.ID, value="username")
# userpass = driver.find_element(By.ID, value="password")

# username = driver.find_element(By.XPATH, value="//input[@name='user-name']")
user = driver.find_element(By.XPATH, value="//input[@placeholder='Username' and @name='user-name']")
userpass = driver.find_element(By.XPATH, value="//input[@name='password']")
button = driver.find_element(By.XPATH, value="//input[@name='login-button']")

# username.send_keys("standard_user")
# time.sleep(2)
user.send_keys("standard_user")
userpass.send_keys("secret_sauce")
time.sleep(2)
button.click()
#
# item1  = driver.find_element(By.XPATH, value="//div[normalize-space()='Sauce Labs Backpack']")
# item1.click()
# time.sleep(2)
#
# itemCart1 = driver.find_element(By.ID, value="add-to-cart")
# itemCart1.click()
# time.sleep(2)
# driver.back()
#
# item2 = driver.find_element(By.XPATH, value="//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
# item2.click()
# time.sleep(2)
#
# cart = driver.find_element(By.XPATH, value="//a[@class='shopping_cart_link']")

# product = driver.find_element(By.XPATH, value="//div[text()='Sauce Labs Onesie']")

# product1 = driver.find_element(By.XPATH, value="//div[contains(text(),'Bolt T-Shirt')]")
# product1.click()





time.sleep(5)

driver.quit()