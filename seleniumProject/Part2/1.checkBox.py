from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Edge()
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
print(driver.title)
time.sleep(2)

# checkbox
checkBoxes = driver.find_elements(By.XPATH, value="//input[@type='checkbox']")
for i in range(len(checkBoxes)):
    if not checkBoxes[i].is_selected():
        checkBoxes[i].click()
time.sleep(5)

# radioButton select Mercedes
radioButtons = driver.find_elements(By.XPATH, value="//input[@type='radio']")
for button in radioButtons:
    btn_id = button.get_attribute("id")
    label = driver.find_element(By.XPATH, f"//label[@for='{btn_id}']").text
    if label == "Mercedes":
        button.click()
time.sleep(5)

driver.quit()