from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.maximize_window()

driver.get("https://www.saucedemo.com/")
time.sleep(2)



time.sleep(5)
driver.close()