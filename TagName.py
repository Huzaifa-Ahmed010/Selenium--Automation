from selenium import webdriver 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")

driver.find_element(By.LINK_TEXT, "Sortable Data Tables").click()

# Get entire table content
# table = driver.find_element(By.TAG_NAME, "table")
# print(table.text)

# To get all rows
# rows = driver.find_elements(By.TAG_NAME, "tr")
# for row in rows:
#     print(row.text)

rows = driver.find_elements(By.TAG_NAME, "tr")

# To get all cells
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        print(cell.text)
driver.quit()