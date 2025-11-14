from itertools import product

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
# time.sleep(2)

# locating using id
# username = driver.find_element(By.ID, value="username")
# userpass = driver.find_element(By.ID, value="password")

# locating using XPATH
# username = driver.find_element(By.XPATH, value="//input[@name='user-name']")
# userpass = driver.find_element(By.XPATH, value="//input[@name='password']")
# button = driver.find_element(By.XPATH, value="//input[@name='login-button']")

# username.send_keys("standard_user")
# time.sleep(2)
# username.send_keys("standard_user")
# userpass.send_keys("secret_sauce")
# time.sleep(2)
# button.click()

# locating using normalize space
# item1  = driver.find_element(By.XPATH, value="//div[normalize-space()='Sauce Labs Backpack']")
# item1.click()
# time.sleep(2)

# itemCart1 = driver.find_element(By.ID, value="add-to-cart")
# itemCart1.click()
# time.sleep(2)
# driver.back()
#
# item2 = driver.find_element(By.XPATH, value="//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
# item2.click()
# time.sleep(2)

# cart = driver.find_element(By.XPATH, value="//a[@class='shopping_cart_link']")

# locating using text Method
# product = driver.find_element(By.XPATH, value="//div[text()='Sauce Labs Onesie']")

# locating using Contains
# product1 = driver.find_element(By.XPATH, value="//div[contains(text(),'Bolt T-Shirt')]")
# product1.click()

# locating using And
# user = driver.find_element(By.XPATH, value="//input[@type='text' and @placeholder='Username' and @name='user-name']")
# userpass = driver.find_element(By.XPATH, value="//input[@type='password'  and @placeholder='Password' and @name='password']")
# button = driver.find_element(By.XPATH, value="//input[@type='submit' and @name='login-button' and @value='Login']")
#
# user.send_keys("standard_user")
# userpass.send_keys("secret_sauce")
# button.click()
# time.sleep(5)

# locating using index
user = driver.find_element(By.XPATH, value="//input[@type='text' and @placeholder='Username' or @name='user-name']")
userpass = driver.find_element(By.XPATH, value="//input[@type='password'  and @placeholder='Password' or @name='password']")
button = driver.find_element(By.XPATH, value="//input[@type='submit' and @name='login-button' and @value='Login' or @value='click here']")

user.send_keys("standard_user")
userpass.send_keys("secret_sauce")
button.click()

productIdx = driver.find_element(By.XPATH, value="(//div[contains(text(),'Sauce Labs')])[2]")
productIdx.click()

time.sleep(5)

driver.quit()