from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()

driver.get("http://www.uitestingplayground.com/alerts")

# alert acceptance
def acceptance():
    alert_btn = driver.find_element(By.XPATH, value="//button[@id='alertButton']")
    alert_btn.click()
    time.sleep(3)
    alert = driver.switch_to.alert
    print("Alert message: ", alert.text)
    alert.accept()

# alert confirm
def confirm():
    alert_btn = driver.find_element(By.XPATH, value="//button[@id='confirmButton']")
    alert_btn.click()
    time.sleep(3)

    alert = driver.switch_to.alert
    print("Alert message: ", alert.text)
    alert.accept() # accept alert
    # alert.dismiss() # reject alert
    time.sleep(3)

    alert2 = driver.switch_to.alert
    print("Second alert: ", alert2.text)
    alert2.accept()

# alert prompt
def prompt():
    alert_btn = driver.find_element(By.XPATH, value="//button[@id='promptButton']")
    alert_btn.click()
    time.sleep(3)

    alert = driver.switch_to.alert
    print("Alert Message: ", alert.text)
    alert.send_keys("Happy Coding")
    time.sleep(3)
    alert.accept()
    time.sleep(3)

    alert2 = driver.switch_to.alert
    print("Second Message: ", alert2.text)
    time.sleep(2)
    alert2.accept()


# acceptance()
# confirm()
prompt()

time.sleep(5)
driver.quit()