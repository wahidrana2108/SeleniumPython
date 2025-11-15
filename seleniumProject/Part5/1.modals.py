from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://practice-automation.com/modals/")

def simple_modal():
    driver.find_element(By.XPATH, value="//button[@id='simpleModal' and @type='button']").click()
    time.sleep(3)

    title = driver.find_element(By.ID, value="pum_popup_title_1318")
    body = driver.find_element(By.XPATH, value="//div[@id='popmake-1318']/div/p")
    print(title.text, "=>", body.text)
    driver.find_element(By.XPATH, value="//button[@aria-label='Close']").click()

def form_modal():
    driver.find_element(By.ID, value="formModal").click()
    time.sleep(2)
    driver.find_element(By.XPATH, value="//input[@name='g1051-name' and @id='g1051-name']").send_keys("ABC")
    driver.find_element(By.XPATH, value="//input[@name='g1051-email' and @id='g1051-email']").send_keys("abc@email.com")
    driver.find_element(By.XPATH, value="//textarea[@name='g1051-message' and @id='contact-form-comment-g1051-message']").send_keys("Hello ABC, Welcome to Selenium.")
    time.sleep(3)
    driver.find_element(By.XPATH, value="//button[@class='pushbutton-wide']").click()
    time.sleep(3)
    info = driver.find_elements(By.XPATH, value="//div[@data-wp-text='context.submission.value']")
    print("Page Title:", driver.title)
    print("Name:", info[0].text)
    print("Email:", info[1].text)
    print("Message:", info[2].text)

# simple_modal()
form_modal()

time.sleep(3)
driver.quit()