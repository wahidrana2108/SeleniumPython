from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.maximize_window()

driver.get("https://www.saucedemo.com/")

# locating using index
user = driver.find_element(By.XPATH, value="//input[@type='text' and @placeholder='Username' or @name='user-name']")
userpass = driver.find_element(By.XPATH, value="//input[@type='password'  and @placeholder='Password' or @name='password']")
button = driver.find_element(By.XPATH, value="//input[@type='submit' and @name='login-button' and @value='Login' or @value='click here']")

user.send_keys("standard_user")
userpass.send_keys("secret_sauce")
button.click()
time.sleep(2)



time.sleep(5)
driver.close()