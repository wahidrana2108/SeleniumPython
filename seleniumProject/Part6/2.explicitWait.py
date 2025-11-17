from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://duckduckgo.com/")

# Explicit Wait
# wait = WebDriverWait(driver, 10)

# Explicit Wait with conditions
wait = WebDriverWait(driver, 10, ignored_exceptions=[NoSuchElementException,TimeoutException,Exception])

textField = wait.until(EC.presence_of_element_located((By.ID, "searchbox_input")))

textField.send_keys("Selenium")
textField.send_keys(Keys.RETURN)
time.sleep(3)
driver.quit()