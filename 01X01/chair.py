import time

def choose(driver, By):
    chairs = driver.find_elements(By.CLASS_NAME, 'seat')
    for chair in chairs:
        if 'available' in chair.get_attribute('class'):
            seat = chair.find_element(By.CSS_SELECTOR, 'span')
            seat.click()
            time.sleep(5)
            nextBtn = driver.find_element(By.CSS_SELECTOR, '.nextbutton-panel>div>button')
            nextBtn.click()
            time.sleep(5)
            break
