from operator import contains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(5)

def tooltip_text():
    driver.get("https://practice.expandtesting.com/tooltips")
    time.sleep(3)
    btns = driver.find_elements(By.CSS_SELECTOR, "[id*='btn']")
    actions = ActionChains(driver)
    for btn in btns:
        print(btn.text)
        actions.move_to_element(btn).perform()
        time.sleep(3)

def google_tooltip():
    driver.get("https://www.google.com/")
    time.sleep(3)
    tip = driver.find_element(By.NAME, "q")
    actions = ActionChains(driver)
    actions.move_to_element(tip).perform()
    time.sleep(3)
    tip_text = tip.get_attribute("title")
    print(tip_text)
    if tip_text == "Search":
        print("Test Passed")
    else:
        print(f"Test Failed. Showing: {tip_text}")

# tooltip_text()
google_tooltip()

time.sleep(5)
driver.quit()