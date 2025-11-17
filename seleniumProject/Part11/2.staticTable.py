from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")

# row count
rows = driver.find_elements(By.XPATH, value="//table[@name='BookTable']//tbody//tr")
print(f"Total rows: {len(rows)}")

# column count
columns = driver.find_elements(By.XPATH, value="//table[@name='BookTable']//tbody//tr[1]//th")
print(f"Total columns: {len(columns)}")

# printing cells using loop
for row in range(2, len(rows)+1):
    for column in range(1, len(columns)+1):
        cell_path = f"//table[@name='BookTable']//tbody//tr[{row}]//td[{column}]"
        data = driver.find_element(By.XPATH, cell_path)
        print(data.text)

time.sleep(3)
driver.quit()