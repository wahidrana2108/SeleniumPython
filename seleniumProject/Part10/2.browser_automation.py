from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
parent_window = driver.current_window_handle
print(parent_window)
driver.implicitly_wait(10)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

window_list = driver.window_handles
for window_id in window_list:
    if window_id != parent_window:
        driver.switch_to.window(window_id)
        print("Switched to new window")
        if driver.title == "Human Resources Management Software | HRMS | OrangeHRM":
            print("Title Verified")
            driver.find_element(By.XPATH, value="//button[text()='Contact Sales']").click()
            time.sleep(2)
            if driver.current_url == "https://www.orangehrm.com/en/contact-sales":
                print("Successfully navigated to Contact Sales page")
                try:
                    driver.close()
                    print("Current window successfully closed")
                    try:
                        driver.switch_to.window(parent_window)
                        print("Successfully Switched to Parent Window")

                        driver.find_element(By.NAME, "username").send_keys("Admin")
                        driver.find_element(By.NAME, "password").send_keys("admin123")
                        time.sleep(3)
                        driver.find_element(By.XPATH, value="//button[@type='submit']").click()

                        time.sleep(3)
                        if driver.title == "OrangeHRM":
                            print("Congratulation! All Test Successfully Passed...")
                    except:
                        print("Failed to Switch to Parent Window")
                except:
                    print(Exception)
        else:
            print("Something went wrong")

time.sleep(5)
driver.quit()