from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(5) # Implicit Wait
driver.get("https://duckduckgo.com/")
textField = driver.find_element(By.ID, value="searchbox_input")
textField.send_keys("Selenium")
textField.send_keys(Keys.RETURN)
time.sleep(3)
driver.quit()