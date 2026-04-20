# Import Selenium WebDriver module
# It is used to control the web browser (open, close, navigate pages)
from selenium import webdriver 
# Import By class
# It is used to locate web elements using different locator strategies
# such as ID, Name, XPath, CSS Selector, Class Name etc.
from selenium.webdriver.common.by import By 
# Import Service class
# It is used to start and manage the browser driver service
# (for example ChromeDriver service)
from selenium.webdriver.chrome.service import Service
# Import ChromeDriverManager
# This automatically downloads and manages the correct ChromeDriver
# version compatible with the installed Chrome browser
from webdriver_manager.chrome import ChromeDriverManager
# Import time module from Python standard library
# It is used to pause the program execution for a few seconds
# (for example time.sleep(3) pauses execution for 3 seconds)
import time

# It is used to start and control the Chrome browser using Selenium WebDriver in Python.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Form Authentication").click()

# driver.find_element(By.PARTIAL_LINK_TEXT, "JavaScript onload").click()
time.sleep(2)

# # Search username element
search_username = driver.find_element(By.NAME, "username").send_keys("tomsmith")

# # Search password element
search_password = driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")
time.sleep(2)

# # click login btn
# driver.find_element(By.CLASS_NAME, "radius").click()
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)

driver.back()
driver.refresh()
driver.quit()