from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

user_field = driver.find_elements(By.TAG_NAME, "input")
print(len(user_field))
for i in range(len(user_field)):
    print(user_field[i].get_attribute("id"))

user_field[0].send_keys("standard_user")
user_field[1].send_keys("secret_sauce")
user_field[2].click()

# find multiple elements using multiple selectors
allProducts = driver.find_elements(By.CLASS_NAME, value="inventory_item_name")
for product in allProducts:
    print(product.text)

time.sleep(2)
driver.quit()