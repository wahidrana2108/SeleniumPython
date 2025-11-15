from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()

def dynamic_search():
    driver.get("https://www.google.com/")
    time.sleep(2)

    bar = driver.find_element(By.NAME, value="q")
    bar.send_keys("wahidrana2108 github")
    time.sleep(2)
    suggestions = driver.find_elements(By.XPATH, value="//ul[@role='listbox']//li")

    for suggestion in suggestions:
        print(suggestion.text)

dynamic_search()
time.sleep(3)
driver.quit()