import time

user_name = "your-name"
user_family = "your-family"
user_mobile = "your-mobile"
user_code = "your-code"

def insert(driver, By):
    mobile = driver.find_element(By.NAME, 'rMobile')
    code = driver.find_element(By.NAME, 'rcode')
    name = driver.find_element(By.NAME, 'rName')
    family = driver.find_element(By.NAME, 'rLName')
    btn = driver.find_element(By.CLASS_NAME, 'btn-u-blue')

    mobile.send_keys(user_mobile)
    code.send_keys(user_code)
    name.send_keys(user_name)
    family.send_keys(user_family)

    time.sleep(2)

    btn.click()