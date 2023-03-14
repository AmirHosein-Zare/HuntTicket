from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

# set browser
driver = webdriver.Chrome()
driver.maximize_window()  
# get url
driver.get("https://safar724.com/bus/tehran-shiraz?date=1401/12/25")

flag = True
while(flag):
    window = driver.find_element(By.TAG_NAME, "html")
    for i in range(3):
        # get elements
        elements = driver.find_elements(By.CSS_SELECTOR, '.available-seat>span')
        # check amount
        for element in elements:
            if int(element.text) > 0:

                print('buy')
                flag = False
        try:
            window.send_keys(Keys.PAGE_DOWN)
        except:
            i -= 1
            pass
        time.sleep(5)
    # refresh the page
    driver.refresh()
    time.sleep(5)
