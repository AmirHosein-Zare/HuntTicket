from selenium.webdriver.common.by import By
from selenium import webdriver
from email import PyEmailer

# set browser
driver = webdriver.Chrome()
driver.maximize_window()  
# get url
driver.get("https://safar724.com/bus/tehran-shiraz?date=1401/12/25")



for i in range(100000000000000000):
    # get elements
    elements = driver.find_elements(By.CSS_SELECTOR, '.available-seat>span')
    # check amount
    for element in elements:
        if element.text > 0:
            print('buy')
            break
