from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("http://www.google.com")
time.sleep(2)
driver.get("http://www.youtube.com")
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.quit()