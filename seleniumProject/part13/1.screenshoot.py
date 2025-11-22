from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

folder_path = r"D:\Selenium Python\seleniumProject\part13"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.saucedemo.com")
time.sleep(2)

full_page_path = folder_path + "\\fullpage.png"
driver.get_screenshot_as_file(full_page_path)
print(full_page_path)

element = driver.find_element(By.ID, "login-button")
element_path = folder_path + "\\element.png"
element.screenshot(element_path)
print(element_path)

section = driver.find_element(By.ID, "login_credentials")
section_path = folder_path + "\\section.png"
section.screenshot(section_path)
print(section_path)


driver.quit()