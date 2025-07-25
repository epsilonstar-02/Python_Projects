from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.70334372128242%2C%22north%22%3A37.84716911473808%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
FORM_URL = "YOUR_GOOGLE_FORM_URL"

class DataEntryBot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.properties = []

    def get_property_data(self):
        self.driver.get(ZILLOW_URL)
        time.sleep(5)

        listings = self.driver.find_elements(By.CSS_SELECTOR, ".list-card")

        for listing in listings:
            try:
                address = listing.find_element(By.CSS_SELECTOR, ".list-card-addr").text
                price = listing.find_element(By.CSS_SELECTOR, ".list-card-price").text
                link = listing.find_element(By.CSS_SELECTOR, ".list-card-link").get_attribute("href")
                self.properties.append({"address": address, "price": price, "link": link})
            except:
                continue

    def fill_form(self):
        for prop in self.properties:
            self.driver.get(FORM_URL)
            time.sleep(2)

            address_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')

            address_input.send_keys(prop["address"])
            price_input.send_keys(prop["price"])
            link_input.send_keys(prop["link"])
            submit_button.click()

    def save_to_csv(self):
        with open("Zillow.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["address", "price", "link"])
            writer.writeheader()
            writer.writerows(self.properties)

bot = DataEntryBot()
bot.get_property_data()
bot.save_to_csv()

