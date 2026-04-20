from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.amazon.com/gp/aw/d/B0F3MMK1J4/ref=ox_sc_act_image_1?smid=ATVPDKIKX0DER&psc=1")

# find search box
search = driver.find_element(By.CLASS_NAME, "celwidget")
print(search.text)
# type text to find
# search.send_keys("Selenium with python GFG")

time.sleep(2)

driver.quit()
