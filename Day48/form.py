from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://secure-retreat-92358.herokuapp.com")

driver.find_element(By.NAME, "fName").send_keys("Abdul")
driver.find_element(By.NAME, "lName").send_keys("Rahman")
driver.find_element(By.NAME, "email").send_keys("unknownemail@gmail.com")
driver.find_element(By.CSS_SELECTOR, "button").click()

driver.quit()