from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

#Text field
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
for i in range(0,2):
    driver.find_element(By.ID,'female').click()
    sleep(2)
    driver.find_element(By.ID,'male').click()
driver.quit()