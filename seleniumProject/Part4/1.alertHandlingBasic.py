from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://demo.guru99.com/V4/index.php")

loginBtn = driver.find_element(By.XPATH, value="//input[@name='btnLogin' and @value='LOGIN']")
loginBtn.click()
time.sleep(3)

alert = driver.switch_to.alert
print("Alert Message: ", alert.text)
alert.accept()

time.sleep(3)
driver.quit()