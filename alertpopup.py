from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome()
driver.get("https://example.com")

alert = (driver, 10).until(ec.alert_is_present())
print(alert.text)
# accept alert
alert.accept()

# dismiss alert 
alert.dismiss()

# prompt alert
alert.send_keys("Huzaifa")
alert.accept()


driver.quit()
