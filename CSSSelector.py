from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/")
    # driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)

    wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Form Authentication"))).click()
    

    driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("tomsmith")

    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("SuperSecretPassword!")


    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    print("login successful...")
except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()