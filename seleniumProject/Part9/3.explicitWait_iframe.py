from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("http://127.0.0.1:5500/iframePracticeSite/nested-frame.html")
time.sleep(3)

parent_frame = driver.find_elements(By.NAME, "parentFrame")

if parent_frame:
    count_main = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"Root iframe count:{len(count_main)}")
    try:
        # switch to parent frame
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "parentFrame")))

        count_parent = driver.find_elements(By.TAG_NAME, "iframe")
        print(f"Parent iframe count:{len(count_parent)}")

        head = driver.find_element(By.TAG_NAME, "h3")
        para = driver.find_element(By.TAG_NAME, "p")
        print(f"Parent frame: {head.text} => {para.text}")

        try:
            # switch to child frame
            WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "childFrame")))

            count_child = driver.find_elements(By.TAG_NAME, "iframe")
            print(f"Child iframe count:{len(count_child)}")

            c_head = driver.find_element(By.TAG_NAME, "h4")
            c_para = driver.find_element(By.ID, "childText")
            print(f"Child frame: {c_head.text} => {c_para.text}")
            try:
                driver.switch_to.parent_frame()  # switching parent frame
                print("Switched to Parent Frame")
            except:
                print("Failed to Switched to Parent Frame")
        except:
            print(f"Child Error: {Exception}")


    except:
        print(f"Parent Error: {Exception}")

    try:
        driver.switch_to.default_content()
        print("Switched to Default Content")
    except:
        print("Failed to Switched to Default Content")

time.sleep(3)
driver.quit()