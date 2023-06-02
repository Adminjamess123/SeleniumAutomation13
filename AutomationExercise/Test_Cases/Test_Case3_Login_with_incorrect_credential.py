from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import string
import random


# Test Case 3: Login User with incorrect email and password

def test_valid_reistration():
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

    # Step 5 = Verify 'Login to your account' is visible
    expected_login_text = "Login to your account"
    actual_login_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form > h2:nth-child(1)")))
    actual_login_text = actual_login_element.text

    try:
        expected_login_text == actual_login_text
        print("Login to your account is visible successfully")
    except:
        print("Login to your account is not visible successfully")

    # Step 6 = Enter correct email address and password

    # type incorrect email

    login_email = driver.find_element(By.CSS_SELECTOR, ".login-form > form:nth-child(2) > input:nth-child(2)")
    login_email.send_keys("james.gomes7@gmail.com")

    # type incorrect password

    password = driver.find_element(By.CSS_SELECTOR, ".login-form > form:nth-child(2) > input:nth-child(3)")
    password.send_keys("admin12")

    # Step 7 = Click 'login' button
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn:nth-child(4)")))
    login_button.click()

    # Step 8 = Verify error 'Your email or password is incorrect!' is visible
    expected_error_text = "'Your email or password is incorrect!'"
    actual_error_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form > form:nth-child(2) > p:nth-child(4)")))
    actual_error_text = actual_error_element.text

    try:
        expected_error_text == actual_error_text
        print("'Your email or password is incorrect!' is visible successfully")
    except:
        print("'Your email or password is incorrect!' is not visible successfully")





