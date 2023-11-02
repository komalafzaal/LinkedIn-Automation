from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import USERNAME, PASSWORD

SEARCH_TEXT = "hr"

# Create Chrome WebDriver instance
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.linkedin.com")

username = wait.until(EC.visibility_of_element_located((By.ID, "session_key")))
password = wait.until(EC.visibility_of_element_located((By.ID, "session_password")))

# Enter username and password
username.send_keys(USERNAME)
password.send_keys(PASSWORD)

# Click the login button
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/section[1]/div/div/form/div[2]/button")))
login_button.click()
print("Login successful")

# Search for profiles
search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='global-nav-typeahead']/input")))
search_box.send_keys(SEARCH_TEXT)
search_box.send_keys(Keys.RETURN)

# Wait for the "People" filter to be visible and click it
people_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[.//button[text()='People']]//button")))
people_filter.click()

# Find and click the "Connect" buttons (if text is 'Connect')
connect_buttons = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//span[text()='Connect']/ancestor::button")))
for button in connect_buttons[:5]:
    button.click()
    send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'artdeco-button--primary')))
    send_button.click()
    time.sleep(5)

driver.quit()
