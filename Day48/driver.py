from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.python.org")

events_element = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
event = [i.text for i in events_element]
time_element = driver.find_elements(By.CSS_SELECTOR, ".event-widget li time")
time = [i.text for i in time_element]

events = {i: {"time": time[i], "event": event[i]} for i in range(len(event))}
print(events)

driver.quit()