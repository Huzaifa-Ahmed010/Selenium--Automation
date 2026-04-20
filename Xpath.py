from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_field = (By.XPATH, "//input[@id='username']")
        self.password_field = (By.XPATH, "//input[@id='password']")
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")
    
    def enter_username(self, username):
        self.wait.until(ec.presence_of_element_located(self.username_field)).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)
    
    def click_login(self):
        self.wait.until(ec.element_to_be_clickable(self.submit_button)).click()
    
    def close_browser(self):
        self.driver.quit()

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/")
    
    # Click on Form Authentication link
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Form Authentication"))).click()
    
    # Create LoginPage instance and perform login
    login_page = LoginPage(driver)
    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()
    
    print("Login successful!")
    
except Exception as e:
    print(f"Error: {e}")
finally:
    try:
        driver.quit()
    except:
        pass
