from idna.idnadata import scripts
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()

def forgot_pass():
    driver.get("https://www.facebook.com/")
    time.sleep(3)
    # forgot = driver.find_element(By.LINK_TEXT, value="Forgotten password?")
    forgot = driver.find_element(By.PARTIAL_LINK_TEXT, value="Forgotten")
    forgot.click()
    time.sleep(3)

    expected = "Forgotten Password | Can't Log In | Facebook"

    if driver.title == expected:
        print("Test PASSES!")
    else:
        print(f"Test FAILED! Expected {"Forgotten Password | Can't Log In | Facebook"} But Got {driver.title}")

    # fieldEmail = driver.find_element(By.XPATH, value="//input[@type='text' and @id='identify_email']")
    # btnSub = driver.find_element(By.XPATH, value="//button[@id='did_submit' and @type='submit']")
    # fieldEmail.send_keys("018********")
    # btnSub.click()

def css_selector():
    driver.get("https://practice.expandtesting.com/login")
    time.sleep(3)

    # driver.find_element(By.CSS_SELECTOR, value="#username").send_keys("practice") #CSS_SELECTOR
    # driver.find_element(By.CSS_SELECTOR, value="[name='username']").send_keys("practice") #attribute
    driver.find_element(By.CSS_SELECTOR, value="input.form-control").send_keys("practice") #conbination
    driver.find_element(By.CSS_SELECTOR, value="#password").send_keys("SuperSecretPassword!")
    btn = driver.find_element(By.CSS_SELECTOR, value=".btn.btn-bg.btn-primary.d-block.w-100")
    time.sleep(5)

    driver.execute_script("arguments[0].scrollIntoView(true);",btn)
    btn.click()

def css_selector_parent_child():
    driver.get("https://www.facebook.com/")
    time.sleep(3)
    # driver.find_element(By.CSS_SELECTOR, value="div>input#email").send_keys("facebook@gamil.com") #Direct child
    driver.find_element(By.CSS_SELECTOR, value="form input#email").send_keys("facebook@gamil.com") #Descendant
    time.sleep(3)



# forgot_pass()
# css_selector()
css_selector_parent_child()

time.sleep(3)

driver.close()