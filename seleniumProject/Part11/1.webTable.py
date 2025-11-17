from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("D:/Selenium Python/seleniumProject/Part11/SampleTable.html")

# columns count
columns = driver.find_elements(By.XPATH, value="//table//tbody//tr[1]//th")
print(f"Total Column:{len(columns)}")

# row count
rows = driver.find_elements(By.XPATH, value="//table//tbody//tr")
print(f"Total Rows:{len(rows)}")

# loop through column and row
for row in range(2, len(rows)+1):
    for column in range(1,len(columns)+1):
        cell_path = f"//table//tbody//tr[{row}]//td[{column}]"

        data = driver.find_element(By.XPATH, cell_path)
        print(data.text)

time.sleep(2)
driver.quit()