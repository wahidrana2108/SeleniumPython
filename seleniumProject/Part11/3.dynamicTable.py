from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.expandtesting.com/dynamic-table")

# row count
rows = driver.find_elements(By.XPATH, value="//table[@class='table table-striped']//tbody//tr")
print(f"Total rows: {len(rows)}")

# column count
columns = driver.find_elements(By.XPATH, value="//table[@class='table table-striped']//thead//th")
print(f"Total columns: {len(columns)}")

# printing cells using loop
def print_all():
    for row in range(1, len(rows)+1):
        for column in range(1, len(columns)+1):
            cell_path = f"//table[@class='table table-striped']//tbody//tr[{row}]//td[{column}]"
            data = driver.find_element(By.XPATH, cell_path)
            print(data.text)

# printing specific cell data
def print_selected():
    for row in range(1, len(rows)+1):
        element = "Chrome"
        data_path = f"//table[@class='table table-striped']//tr[{row}]//td[1]"
        data = driver.find_element(By.XPATH, data_path)
        if data.text == element:
            cpu_path = f"//table[@class='table table-striped']//tr[{row}]//td[contains(text(),'%')]"
            cpu = driver.find_element(By.XPATH, cpu_path)
            print(f"{element} using {cpu.text} of cpu")

            given = driver.find_element(By.ID, "chrome-cpu").text

            if cpu.text in given:
                print(given)
                print("CPU usage matched!")
                print("All test passed")
            else:
                print("CPU usage not matched!")
            break



# print_all()
print_selected()
time.sleep(5)
driver.quit()