from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
        
    # Initialize Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Navigate to Google
    driver.get("https://www.google.com")
    time.sleep(2)  # Wait for page to load
    
    # Navigate to sweetshop login page
    driver.get("https://sweetshop.vivrichards.co.uk/login")
    time.sleep(2)  # Wait for page to load
    
    # Go back to Google
    driver.back()
    time.sleep(2)
    
    # Go forward to sweetshop login page
    driver.forward()
    time.sleep(2)
    
    # Refresh the current page
    driver.refresh()
    time.sleep(2)
    
    print(f"Page Title: {driver.title}")

    
    driver.quit()
if __name__ == "__main__":
    main()