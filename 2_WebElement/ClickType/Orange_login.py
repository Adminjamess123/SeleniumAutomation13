import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1 = launch browser
driver = webdriver.Firefox()

# Step 2 = open login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

# Step 3 = type username
Username = driver.find_element(By.NAME, "username")
Username.send_keys("Admin")

# Step 4 = type password
Password = driver.find_element(By.NAME, "password")
Password.send_keys("admin123")

# Step 5 = click login button
Login_Button = driver.find_element(By.CSS_SELECTOR, ".oxd-button")
Login_Button.click()
time.sleep(5)

# Step 6 = logout
Profile = driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name")
Profile.click()

Logout = driver.find_element(By.CSS_SELECTOR, ".oxd-dropdown-menu > li:nth-child(4) > a:nth-child(1)")
Logout.click()

driver.close()