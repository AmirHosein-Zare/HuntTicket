from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from mail import alarm
from chair import choose
from person import insert
import time

# set browser
driver = webdriver.Chrome()
driver.maximize_window()  
# get url
driver.get("https://safar724.com/bus/shiraz-bushehr?date=1402-01-03")

flag = True
while(flag):
    window = driver.find_element(By.TAG_NAME, "html")
    for i in range(3):
        # get elements
        elements = driver.find_elements(By.CSS_SELECTOR, '.available-seat>span')
        btns = driver.find_elements(By.CSS_SELECTOR, '.viewseatbtn')
        # check amount
        j=0
        for element in elements:
            if int(element.text) > 0:
                print('buy--------------------')
                # Alarm to buy ticket
                alarm()
                # click on bus btn that have seat
                btns[j].click()
                time.sleep(2)
                # click on btn to choose seat
                seat = driver.find_element(By.CSS_SELECTOR, '#currentSeat>div>div>a')
                seat.click()
                time.sleep(2)
                # choose seat and then click to next page 
                # use chair madule
                choose(driver, By)
                time.sleep(2)
                # insert personal data
                insert()
                flag = False
                break
        try:
            # scroll down to check another ticket
            window.send_keys(Keys.PAGE_DOWN)
        except:
            i -= 1
            pass
        j += 1
        if flag == False:
            break
    # refresh the page
    if flag:
        driver.refresh()
