from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

# single select dropdown
dropDown = Select(driver.find_element(By.ID, value="carBrands"))
if not dropDown.is_multiple:
    print("This is not a MultiSelector")
print(dropDown.first_selected_option.text)
dropDown.select_by_visible_text("Mercedes")
dropDown.select_by_value("mercedes")
time.sleep(5)





driver.quit()