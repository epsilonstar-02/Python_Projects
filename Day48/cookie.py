from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)
language = driver.find_element(By.ID, "langSelect-EN")
language.click()

driver.implicitly_wait(5)

cookie = driver.find_element(By.ID, "bigCookie")
items = driver.find_elements(By.CSS_SELECTOR, "#store .product.unlocked")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 60 * 5
five_sec = time.time() + 5

while True:
    cookie.click()

    if time.time() > five_sec:

        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        money_element = driver.find_element(By.ID, "cookies").text.split(" ")[0]
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        if affordable_upgrades:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
            driver.find_element(By.ID, to_purchase_id).click()

        five_sec = time.time() + 5

    if time.time() > timeout:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break

driver.quit()
