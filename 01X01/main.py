from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# set browser
driver = webdriver.Chrome()
driver.maximize_window()  
# get url
driver.get("https://safar724.com/bus/tehran-shiraz?date=1401/12/25")

elements = driver.find_elements(By.CSS_SELECTOR, '.available-seat>span')


