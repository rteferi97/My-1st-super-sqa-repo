from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import string
import random
import time

url = 'http://dev.bootcamp.store.supersqa.com/'

# Open browser
print("Opening Browser...")
driver = webdriver.Chrome()

# Go to http://dev.bootcamp.store.supersqa.com/
print("going to url...")
driver.get(url)

# Click on ‘my account’
#href="http://dev.bootcamp.store.supersqa.com/my-account/"
print("going to 'my account'")
my_account = driver.find_element(By.LINK_TEXT, 'My account')
my_account.click()

# Type into the registration email and password
#   (Think here do you use the same email all the time or do you generate a random email every time?)
print("typing into registration field...")
letters = string.ascii_lowercase
rand_string = ''.join(random.choice(letters) for i in range(15))
random_email = rand_string + '@supersqa.com'

email_field = driver.find_element(By.ID, 'reg_email')
email_field.send_keys(random_email)


password_field = driver.find_element(By.ID, 'reg_password')
password_field.send_keys(rand_string)

# Click on ‘Register’
print("Registering...")
driver.implicitly_wait(5)
register_button = driver.find_element(By.NAME, 'register')
register_button.click()
print("REGISTERED")

# Verify registration is successful
#   (Hint: look for element that should show up only if registration is successful.
logout_button = driver.find_element(By.CSS_SELECTOR, 'li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout a')

if logout_button.is_displayed():
    logout_button.click()
    print("VERIFIED!")
else:
    raise Exception("User not officially logged in")
# breakpoint()
