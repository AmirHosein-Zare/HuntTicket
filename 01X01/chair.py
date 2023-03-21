def choose(driver, By):
    for i in range(25):
        chair = driver.find_element(By.CSS_SELECTOR, '#' + i)
        if chair.get_attribute('class').find('available'):
            chair.click()
            nextBtn = driver.find_element(By.CSS_SELECTOR, '.nextbutton-panel>div>button')
            nextBtn.click()
