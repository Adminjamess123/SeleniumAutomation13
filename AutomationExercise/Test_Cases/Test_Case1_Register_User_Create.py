import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AutomationExercise.Common import common_functions as CF

def test_valid_reistration():
    # https://automationexercise.com/test_cases
    # Test Case 1: Register User

    user_credentials = [CF.random_email(), CF.random_number(), CF.random_string()]

    filename = "./user_credentials"
    CF.store_user_data(filename, user_credentials)

    # Step 1 = launch browser
    driver = webdriver.Firefox()

    # Step 2 = Open home page
    driver.get("https://automationexercise.com/")

    # Step 3 = Verify that home page is visible successfully
    expected_home_page_url = "https://automationexercise.com/"
    actual_home_page_url = driver.current_url

    try:
        assert expected_home_page_url == actual_home_page_url
        print("Home page is visible successfully")
    except AssertionError:
        print("Home page is not visible successfully")

    # Step 4 = Click on 'Signup / Login' button
    signup_login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[href='\/login']")))
    signup_login_button.click()

    # Step 5 = Verify 'New User Signup!' is visible
    expected_new_user_signup_text = "New User Signup!"
    actual_new_user_signup_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".signup-form > h2")))
    actual_new_user_signup_text = actual_new_user_signup_element.text

    try:
        expected_new_user_signup_text == actual_new_user_signup_text
        print("New User Signup! is visible successfully")
    except:
        print("New User Signup! is not visible successfully")

    # Step 6 = type username
    try:
        Username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[type='text']")))
        Username.send_keys(user_credentials[2])
    except:
        print("Username Locator Changed")

    # Step 7 = type email
    try:
        Email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[action='\/signup'] [type='email']")))
        Email.send_keys(user_credentials[0])
    except:
        print("Email Locator Changed")

    # Step 8 = signup
    signup_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[action='\/signup'] .btn-default")))
    signup_button.click()

    # Step 9 = Verify that 'ENTER ACCOUNT INFORMATION' is visible
    expected_enter_account_information_text = "ENTER ACCOUNT INFORMATION"
    actual_enter_account_information_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form > .text-center.title > b")))
    actual_enter_account_information_text = actual_enter_account_information_element.text

    try:
        expected_enter_account_information_text == actual_enter_account_information_text
        print("ENTER ACCOUNT INFORMATION is visible successfully")
    except:
        print("ENTER ACCOUNT INFORMATION is not visible successfully")

    # Step 6 = click gender title
    title_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#id_gender1")))
    title_button.click()

    # Step 7 = type password
    password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))
    password.send_keys(user_credentials[1])

    # Step 8 = type birth date
    date = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#days"))))
    date.select_by_visible_text("20")

    month = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#months"))))
    month.select_by_visible_text("June")

    year = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#years"))))
    year.select_by_visible_text("2010")

    # Step 9 = click checkbox newsletter
    newsletter_button = driver.find_element(By.CSS_SELECTOR, "#newsletter")
    newsletter_button.click()

    # Step 10 = click checkbox special offer
    offer_button = driver.find_element(By.CSS_SELECTOR, "#optin")
    offer_button.click()

    # Step 11 = type firstname
    try:
        Firstname = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#first_name")))
        Firstname.send_keys(CF.random_string())
    except:
        print("Firstname Not Found")

    # Step 12 = type lastname
    lastname = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#last_name")))
    lastname.send_keys(CF.random_string())

    # Step 13 = type address
    address = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#address1")))
    address.send_keys(CF.random_string())

    # Step 14 = select country
    country = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#country"))))
    country.select_by_visible_text("Canada")

    # Step 15 = type state
    state = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#state")))
    state.send_keys(CF.random_string())

    # Step 16 = type city
    city = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#city")))
    city.send_keys(CF.random_string())

    # Step 17 = type zipcode
    zipcode = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#zipcode")))
    zipcode.send_keys("700001")

    # Step 18 = type mobile number
    mobile_number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mobile_number")))
    mobile_number.send_keys("01817630333")

    # Step 19 = create account
    create = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[action] .btn-default")))
    create.click()

    # Step 20 = Verify that 'ACCOUNT CREATED!' is visible
    expected_account_created_text = "ACCOUNT CREATED!"
    actual_account_created_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".title > b:nth-child(1)")))
    actual_account_created_text = actual_account_created_element.text

    try:
        expected_account_created_text == actual_account_created_text
        print("ACCOUNT CREATED! is visible successfully")
    except:
        print("ACCOUNT CREATED! is not visible successfully")

    # Step 21 = Click 'Continue' button
    Continue = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn")))
    Continue.click()

    # Step 22 = Verify that 'Logged in as username' is visible
    expected_login_username_text = "Logged in as" + user_credentials[2]
    actual_login_username_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar-nav > li:nth-child(10) > a:nth-child(1)")))
    actual_login_username_text = actual_login_username_element.text

    try:
        expected_login_username_text == actual_login_username_text
        print("Logged in as ", user_credentials[2] + " is visible")
    except:
        print("Logged in as ", user_credentials[2] + " is not visible ")

    # driver.close()

    print(user_credentials)