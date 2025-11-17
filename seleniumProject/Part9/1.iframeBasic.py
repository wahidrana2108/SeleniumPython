from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("http://127.0.0.1:5500/iframePracticeSite/index.html")

# left frame
def left_frame():
    driver.switch_to.frame("leftFrame") # switching iframe by id
    driver.find_element(By.NAME, "name").send_keys("iframe")
    driver.find_element(By.NAME, "email").send_keys("iframe@email.com")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']").click()
    driver.switch_to.default_content()

# right frame
def right_frame():
    driver.switch_to.frame(1) # switching iframe by index
    driver.find_element(By.XPATH, value="//button[normalize-space()='Click Me']").click()
    time.sleep(3)
    driver.switch_to.alert.accept()
    time.sleep(3)
    # dropdown select
    option = "Option Two"
    driver.find_element(By.ID, "options").click()
    driver.find_element(By.XPATH, value=f"//select//option[text()='{option}']").click()
    driver.switch_to.default_content()

# bottom frame
def bottom_frame():
    frame = driver.find_element(By.XPATH, value="//iframe[@name='bottomFrame']") # switching iframe by xpath
    driver.switch_to.frame(frame)
    head = driver.find_element(By.TAG_NAME, "h2")
    para = driver.find_element(By.TAG_NAME, "p")
    print(f"{head.text} => {para.text}")
    driver.switch_to.default_content()

# left_frame()
# right_frame()
bottom_frame()
time.sleep(3)
driver.quit()
