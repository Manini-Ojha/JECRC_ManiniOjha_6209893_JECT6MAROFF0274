from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)


driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

days=driver.find_elements(By.XPATH,'//div[@class="form-group"][4]/child::div')
for day in days:
    day.click()
    print(day.text)
    sleep(2)
for day in days[::-1]:
    day.click()
    sleep(2)
