import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to get a real temporary email
def get_temp_email():
    response = requests.post("https://api.mail.tm/accounts", json={
        "address": f"insta_{int(time.time())}@mail.tm",
        "password": "securepassword"
    })
    
    if response.status_code == 201:
        email_data = response.json()
        return email_data["address"], email_data["id"], email_data["password"]
    else:
        raise Exception("Failed to generate a temporary email.")

# Get a real temporary email
email, email_id, email_password = get_temp_email()

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

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
full_name_input.send_keys("John Doe")  # Static Name for Testing
username_input.send_keys("john_doe_987654")  # Adjust to avoid duplicates
password_input.send_keys("Secure@1234")

# Wait for submit button to be clickable and click it
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
)
submit_button.click()

# Wait for email verification
time.sleep(10)

print(f"Temporary Email Used: {email}")
