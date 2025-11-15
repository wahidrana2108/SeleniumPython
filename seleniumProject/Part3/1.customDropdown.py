from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()

def select_custom_option():
    driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
    time.sleep(3)

    dropdown = driver.find_element(By.ID, value="custom-select")
    # scroll down to element
    driver.execute_script("arguments[0].scrollIntoView(true)", dropdown)
    time.sleep(2)
    dropdown.click()

    fav = "Blue"
    fav2 = "Green"
    color = driver.find_element(By.XPATH, value=f"//div[@class='custom-options']/div[text()='{fav}']")
    color.click()
    time.sleep(5)
    dropdown.click()
    color2 = driver.find_element(By.XPATH, value=f"//div[@class='custom-options']/div[text()='{fav2}']")
    color2.click()

select_custom_option()
time.sleep(3)
driver.quit()