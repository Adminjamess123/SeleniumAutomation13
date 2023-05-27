
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random
def random_email():
    domain = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    letters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(letters) for _ in range(15))
    domain_name = random.choice(domain)
    email = f"{username}@{domain_name}"
    return email

def random_string():
    letters = string.ascii_lowercase + string.digits
    random_name = ''.join(random.choice(letters) for _ in range(15))
    string_random = f"{random_name}"
    return string
print(random_string())



# Step 1 = launch browser
driver = webdriver.Firefox()

# Step 2 = open login page
driver.get("https://automationexercise.com/login")

# Step 3 = type username
Username = WebDriverWait(driver, 10). until(EC.presence_of_element_located(By.NAME, "name"))
Username.send_keys("James")

# Step 4 = type email
signup_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > input[type=email]:nth-child(3)"))
signup_email.send_keys(random_email())

# Step 5 = signup
signup_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > button"))
signup_button.click()

# Step 6 = click gender title
title_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#id_gender1"))
title_button.click()

# Step 7 = type password
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#password"))
password.send_keys("admin123")

# Step 8 = type birth date
date = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#days"))
date.select_by_visible_text("10")

month = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#months"))
month.select_by_visible_text("June")

year = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#years"))
year.select_by_visible_text("2010")

# Step 9 = click checkbox newsletter
newsletter_button = driver.find_element(By.CSS_SELECTOR, "#newsletter")
newsletter_button.click()

# Step 10 = click checkbox special offer
offer_button = driver.find_element(By.CSS_SELECTOR, "#optin")
offer_button.click()

# Step 11 = type firstname
firstname = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#first_name"))
firstname.send_keys("James")

# Step 12 = type lastname
lastname = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#last_name"))
lastname.send_keys("Gomes")

# Step 13 = type address
address = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#address1"))
address.send_keys("41/6 North Baridhara")

# Step 14 = select country
country = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#country"))
country.select_by_visible_text("Canada")

# Step 15 = type state
state = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#state"))
state.send_keys("West Bengal")

# Step 16 = type city
city = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#city"))
city.send_keys("Kolkata")

# Step 17 = type zipcode
zipcode = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#zipcode"))
zipcode.send_keys("700001")

# Step 18 = type mobile number
mobile_number = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#mobile_number"))
mobile_number.send_keys("01817630333")

# Step 19 = create account
create = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "[action] .btn-default"))
create.click()


