from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get("https://practice.expandtesting.com/login")
driver.maximize_window()

def test_login():
    username = driver.find_element(By.ID, value="username")
    userpass = driver.find_element(By.ID, value="password")
    # logBtn = driver.find_element(By.ID, value="submit-login")
    # logBtn = driver.find_element(By.XPATH, value="//button[contains(@class, 'btn-primary')]")
    logBtn = driver.find_element(By.XPATH, value="//button[text()='Login' and @id='submit-login']")

    username.send_keys("practice")
    userpass.send_keys("SuperSecretPassword!")
    time.sleep(5)

    logBtn.click()
    time.sleep(5)

    # logOut = driver.find_element(By.XPATH, value="//i[@class='icon-2x icon-signout']")
    logOut = driver.find_element(By.XPATH, value="//i[text()=' Logout']")
    logOut.click()

test_login()
time.sleep(5)
driver.quit()