from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.expandtesting.com/")

# link = driver.find_element(By.LINK_TEXT, value="Test Login Page")
link = driver.find_element(By.PARTIAL_LINK_TEXT, value="Login")

driver.execute_script("arguments[0].scrollIntoView[true]",link)
time.sleep(2)
link.click()

time.sleep(3)
driver.quit()