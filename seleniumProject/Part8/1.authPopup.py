from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

head = driver.find_element(By.XPATH, value="//h3")
para = driver.find_element(By.XPATH, value="//p")
print(f"{head.text} => {para.text}")

time.sleep(3)
driver.quit()