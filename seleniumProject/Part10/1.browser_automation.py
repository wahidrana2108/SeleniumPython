from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from trio import current_time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

# current window id of browser
parent_window_id = driver.current_window_handle
print(parent_window_id)

driver.find_element(By.LINK_TEXT, "Click Here").click()

windows_list = driver.window_handles
print(windows_list)

for window_id in windows_list:
    if window_id != parent_window_id:
        driver.switch_to.window(window_id)
        print(f"Switched to Window ID:{window_id}")
        if driver.title == "New Window":
            print("Window switched successfully")
            current = driver.current_window_handle
            print(current)

            if driver.current_url == "https://the-internet.herokuapp.com/windows/new":
                print("URL Verified!")
                text = driver.find_element(By.TAG_NAME, "h3")
                print(f"New page content: {text.text}")
            else:
                print("Something went Wrong!")

time.sleep(2)

driver.quit()
