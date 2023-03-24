import time

def choose(driver, By):
    # get all chairs
    chairs = driver.find_elements(By.CLASS_NAME, 'seat')
    # loop for check available chair
    for chair in chairs:
        if 'available' in chair.get_attribute('class'):
            # click on available chair
            seat = chair.find_element(By.CSS_SELECTOR, 'span')
            seat.click()
            time.sleep(5)
            # click to next page
            nextBtn = driver.find_element(By.CSS_SELECTOR, '.nextbutton-panel>div>button')
            nextBtn.click()
            time.sleep(5)
            break
