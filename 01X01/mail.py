from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

# set browser
driver = webdriver.Edge()
driver.maximize_window()  
# get url
driver.get("https://safar724.com/bus/tehran-shiraz?date=1401/12/25")

window = driver.find_element(By.CSS_SELECTOR, "body")
window.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
window.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
window.send_keys(Keys.PAGE_DOWN)