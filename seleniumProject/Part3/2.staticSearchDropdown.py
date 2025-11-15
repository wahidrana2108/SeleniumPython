from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()

def select_car():
    driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

    searchableDropdown = driver.find_element(By.CLASS_NAME, value="search-box")
    driver.execute_script("arguments[0].scrollIntoView(true)", searchableDropdown)
    time.sleep(2)
    searchableDropdown.click()

    searchableDropdown.send_keys("s")
    time.sleep(2)
    car = "SUV"
    car2 = "Sedan"
    driver.find_element(By.XPATH, value=f"//div[@class='searchable-options']/div[text()='{car2}']").click()

select_car()
time.sleep(3)
driver.quit()