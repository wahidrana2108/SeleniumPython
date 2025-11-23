from selenium import webdriver
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(2)

driver.switch_to.new_window("tab")
driver.get("https://www.youtube.com/")
time.sleep(2)

driver.switch_to.new_window("window")
driver.get("https://www.facebook.com/")
time.sleep(2)


handles = driver.window_handles

# switching tabs by tab index
# driver.switch_to.window(handles[0])
# time.sleep(2)
# print("Step 1:" + driver.title)
# driver.close()
#
# driver.switch_to.window(handles[1])
# time.sleep(2)
# print("Step 2:" + driver.title)
# driver.close()
#
# driver.switch_to.window(handles[2])
# time.sleep(2)
# print("Step 3:" + driver.title)

# switching tabs by tab title
# target = "YouTube"
# for handle in handles:
#     driver.switch_to.window(handle)
#     if driver.title == target:
#         time.sleep(2)
#         print("Closed:" + driver.title)
#         time.sleep(2)
#         driver.close()
#         break

# switching tabs by tab url
target = "https://www.facebook.com"
for handle in handles:
    driver.switch_to.window(handle)
    if driver.current_url.startswith(target):
        print("Closed:" + driver.title)
        time.sleep(2)
        driver.close()
        break

time.sleep(5)
driver.quit()


