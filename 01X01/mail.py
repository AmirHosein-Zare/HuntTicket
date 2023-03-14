from selenium import webdriver
import time

# set browser
driver = webdriver.Edge()
driver.maximize_window()  
# get url
driver.get("https://aspb2.asset.aparat.com/aparat-video/7cb8f957bb4c61b5f016b87a8a00439515756123-144p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjU5NTBiNGExNTc3Y2E1MmEyYmM4NWQwZGRjODMyNzhmIiwiZXhwIjoxNjc4ODA1NjI4LCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.jEUhGDkgjqxXkwzWZ3svaRQoWz1lcNk44PRejsvdgt4")

time.sleep(60)