from selenium import webdriver
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(2)
print(driver.title)

# driver.switch_to.new_window("tab")
driver.switch_to.new_window("window")
driver.get("https://www.saucedemo.com")
time.sleep(2)
print(driver.title)


handles = driver.window_handles
driver.switch_to.window(handles[0])
time.sleep(2)
print(driver.title)


driver.close()