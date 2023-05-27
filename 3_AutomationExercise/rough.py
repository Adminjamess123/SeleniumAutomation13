
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

print (random_email())

def random_string():
    letters = string.ascii_lowercase + string.digits
    random_name = ''.join(random.choice(letters) for _ in range(5))
    string_random = f"{random_name}"
    return string
print(random_string())