from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("http://127.0.0.1:5500/iframePracticeSite/nested-frame.html")

def count_iframe():
    count_main = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"Root iframe count:{len(count_main)}")
    driver.switch_to.frame("parentFrame")
    count_parent = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"Parent iframe count:{len(count_parent)}")
    driver.switch_to.frame("childFrame")
    count_child = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"Child iframe count:{len(count_child)}")

def dynamic_iframe_count():
    count_main = driver.find_elements(By.TAG_NAME, "iframe")
    if len(count_main) > 1:
        print("No iFrame")
    else:
        print(f"Root iframe count:{len(count_main)}")


def nested_iframe():
    driver.switch_to.frame("parentFrame") #  switching iframe by name

    head = driver.find_element(By.TAG_NAME, "h3")
    para = driver.find_element(By.TAG_NAME, "p")
    print(f"Parent frame: {head.text} => {para.text}")

    driver.switch_to.frame("childFrame")

    c_head = driver.find_element(By.TAG_NAME, "h4")
    c_para = driver.find_element(By.TAG_NAME, "p")
    print(f"Child frame: {c_head.text} => {c_para.text}")
    driver.switch_to.default_content()

def switch_to_parent():
    driver.switch_to.frame("parentFrame") #  switching iframe by name
    driver.switch_to.frame("childFrame")

    c_head = driver.find_element(By.TAG_NAME, "h4")
    c_para = driver.find_element(By.TAG_NAME, "p")
    print(f"Child frame: {c_head.text} => {c_para.text}")
    driver.switch_to.parent_frame() #  switching parent frame

    head = driver.find_element(By.TAG_NAME, "h3")
    para = driver.find_element(By.TAG_NAME, "p")
    print(f"Parent frame: {head.text} => {para.text}")
    driver.switch_to.default_content()

# count_iframe()
dynamic_iframe_count()
# nested_iframe()
# switch_to_parent()
time.sleep(3)
driver.quit()
