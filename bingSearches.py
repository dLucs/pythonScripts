from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
browser.get("https://www.bing.com/?setlang=es")

for i in range(30):
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys(i)
    search_box.submit()
    time.sleep(6)
