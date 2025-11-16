from http.client import responses

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(5)

def practice():
    driver.get("https://practice.expandtesting.com/")

    links = driver.find_elements(By.TAG_NAME, "a")
    valid=0
    broken=0
    for link in links:

        url = link.get_attribute("href")
        response = requests.head( url )

        if response.status_code < 400:
            valid+=1
        else:
            broken+=1
    print(f"Valid links:{valid} and Broken links:{broken}")


def dead_city():
    driver.get("http://www.deadlinkcity.com/")

    links = driver.find_elements(By.XPATH, value="//a")
    valid=0
    broken=0
    for link in links:

        url = link.get_attribute("href")
        try:
            response = requests.head(url, timeout=5)
            if response.status_code < 400:
                valid += 1
            else:
                broken += 1
        except:
            print(f"Error message: {Exception}")


    print(f"Valid links:{valid} and Broken links:{broken}")


# practice()
dead_city()
time.sleep(3)
driver.quit()