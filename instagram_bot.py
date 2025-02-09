from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from faker import Faker

# Set up WebDriver (Auto-download ChromeDriver)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Initialize Faker to generate fake data
fake = Faker()

# Function to generate fake email, name, username, and password
def generate_fake_credentials():
    email = fake.email()
    full_name = fake.name()
    username = fake.user_name()
    password = fake.password(length=10)
    return email, full_name, username, password

# Generate fake credentials
email, full_name, username, password = generate_fake_credentials()

# Open Instagram signup page
driver.get('https://www.instagram.com/accounts/emailsignup/')

# Wait for the page to load
time.sleep(5)

# Find input fields and fill them
email_input = driver.find_element(By.NAME, 'emailOrPhone')
full_name_input = driver.find_element(By.NAME, 'fullName')
username_input = driver.find_element(By.NAME, 'username')
password_input = driver.find_element(By.NAME, 'password')

email_input.send_keys(email)
full_name_input.send_keys(full_name)
username_input.send_keys(username)
password_input.send_keys(password)

# Wait for submit button to be clickable and click it
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
)
submit_button.click()

# Wait for account creation to complete
time.sleep(10)



