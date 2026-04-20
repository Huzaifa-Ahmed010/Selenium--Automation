from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_field = (By.CSS_SELECTOR, "input[type='email']")
        self.password_field = (By.CSS_SELECTOR, "input[type='password']")
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")
    
    def enter_username(self, username):
        if username == "testing@aivoa.net":
            self.wait.until(ec.presence_of_element_located(self.username_field)).send_keys(username)
        else:
            print("Invalid Email..")
    def enter_password(self, password):
        if password == "password123":
            self.driver.find_element(*self.password_field).send_keys(password)
        else:
            print("Invalid password..")
    def click_login(self):
        self.wait.until(ec.element_to_be_clickable(self.submit_button)).click()
        time.sleep(2)
    def close_browser(self):
        self.driver.quit()

try:
    for i in range(0, 1):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("http://216.48.184.249:5289/login")
        
       
        login_page = LoginPage(driver)
        login_page.enter_username("testing@aivoa.net")
        login_page.enter_password("password123")
        login_page.click_login()
    
except Exception as e:
    print(f"Error: {e}")
finally:
    try:
        driver.quit()
    except:
        pass
