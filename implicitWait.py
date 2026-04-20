from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#create driver object 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#implicit wait
driver.implicitly_wait(10)

# open url
driver.get("https://www.google.com/")

try:
    element = driver.find_element(By.CLASS_NAME, "truncate").send_keys("Testing Bootcamp")
    element.click()
    print("Search bar found!")
finally:
    driver.quit()
