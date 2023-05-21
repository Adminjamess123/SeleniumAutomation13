from selenium import webdriver

# Launch Browser
driver = webdriver.Firefox()

# Open Website
driver.get("https://www.google.com/")

# Close current tab
driver.close()

# To close the whole browser with one or more ope tab command should be "driver.quit()"

