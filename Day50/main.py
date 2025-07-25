from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

FB_EMAIL = "YOUR_FACEBOOK_EMAIL"
FB_PASSWORD = "YOUR_FACEBOOK_PASSWORD"

driver = webdriver.Firefox()
driver.get("http://www.tinder.com")

time.sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_button.click()

time.sleep(2)
fb_login = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
password_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
email_input.send_keys(FB_EMAIL)
password_input.send_keys(FB_PASSWORD)
password_input.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)

time.sleep(5)
allow_location_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    time.sleep(1)
    try:
        like_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()

