from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#create driver object 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# open url
driver.get("https://restful-api.dev/")

try:
    # wait up to 10 sec for element to be present
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CLASS_NAME, "MuiButtonBase-root")).click()
    print("element found!")

finally:
    driver.quit()