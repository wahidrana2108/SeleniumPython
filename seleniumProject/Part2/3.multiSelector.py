from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
multiSelect = Select(driver.find_element(By.ID, "multiSelect"))
if multiSelect.is_multiple:
    print("This is a MultiSelector")

# multiSelect.select_by_visible_text("Mercedes")
# multiSelect.select_by_visible_text("Audi")
# multiSelect.select_by_visible_text("Volvo")
allOptions = multiSelect.options
for option in allOptions:
    multiSelect.select_by_visible_text(option.text)
time.sleep(5)

# multiSelect.deselect_by_visible_text("Volvo")
multiSelect.deselect_all()
time.sleep(5)

selected_option = multiSelect.all_selected_options
for option in selected_option:
    print(option.text)
time.sleep(5)
driver.quit()