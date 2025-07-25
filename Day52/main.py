from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

INSTAGRAM_EMAIL = "YOUR_INSTAGRAM_EMAIL"
INSTAGRAM_PASSWORD = "YOUR_INSTAGRAM_PASSWORD"
SIMILAR_ACCOUNT = "chiefpat"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        email_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        email_input.send_keys(INSTAGRAM_EMAIL)
        password_input.send_keys(INSTAGRAM_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(5)
        followers_link = self.driver.find_element(By.XPATH, f'//a[contains(@href, "/{SIMILAR_ACCOUNT}/followers/")]')
        followers_link.click()
        time.sleep(5)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

