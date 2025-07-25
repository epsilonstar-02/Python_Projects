from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()
article_count = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/ul/li[2]/a[1]")
print(article_count.text)

driver.quit()