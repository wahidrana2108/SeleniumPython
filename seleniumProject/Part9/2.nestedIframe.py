from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("http://127.0.0.1:5500/seleniumProject/iframePracticeSite/nested-frame.html")

def nested_iframe():
    driver.switch_to.frame("parentFrame") #  switching iframe by name

    head = driver.find_element(By.TAG_NAME, "h3")
    para = driver.find_element(By.TAG_NAME, "p")
    print(f"Parent frame: {head.text} => {para.text}")

    driver.switch_to.frame("childFrame")

    cHead = driver.find_element(By.TAG_NAME, "h4")
    cPara = driver.find_element(By.TAG_NAME, "p")
    print(f"Child frame: {cHead.text} => {cPara.text}")

nested_iframe()
time.sleep(3)
driver.quit()
