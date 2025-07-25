from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "YOUR_EMAIL"
ACCOUNT_PASSWORD = "YOUR_PASSWORD"
PHONE = "YOUR_PHONE_NUMBER"
JOB_SEARCH_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"


driver = webdriver.Firefox()
driver.get(JOB_SEARCH_URL)

time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(2)
email_input = driver.find_element(By.ID, "username")
email_input.send_keys(ACCOUNT_EMAIL)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(ACCOUNT_PASSWORD)
password_input.send_keys(Keys.ENTER)

time.sleep(5) 

job_listings = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")

for job in job_listings:
    job.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()

        time.sleep(2)
        phone_input = driver.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
        if phone_input.text == "":
            phone_input.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if "Submit" in submit_button.text:
            submit_button.click()
            print("Application submitted.")
        else:
            close_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
            close_button.click()
            time.sleep(1)
            discard_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar .artdeco-button--secondary")
            discard_button.click()
            print("Complex application, skipped.")

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

driver.quit()
