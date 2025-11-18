from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://practice.expandtesting.com/tooltips")

btn_top = driver.find_element(By.ID, "btn1")

actions = ActionChains(driver)
actions.move_to_element(btn_top).perform()

time.sleep(5)
driver.quit()