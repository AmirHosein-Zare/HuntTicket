from selenium.webdriver.common.by import By
from selenium import webdriver

# set browser
driver = webdriver.Chrome()
driver.maximize_window()
# get url
driver.get("https://mail.google.com/mail/u/0/#inbox")

