user_name = "امیرحسین"
user_family = "زارع"
user_mobile = "09172535548"
user_code = "2520185740"

def input(driver, By):
    mobile = driver.find_element(By.NAME, 'rMobile')
    code = driver.find_element(By.NAME, 'rcode')
    name = driver.find_element(By.NAME, 'rName')
    family = driver.find_element(By.NAME, 'rLName')
    btn = driver.find_element(By.CLASS_NAME, 'btn-u-blue')

    