from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://opensource-demo.orangehrmlive.com/")
sleep(5)
print(driver.title)
username=driver.find_element(By.XPATH,'//input[@name="username"]')
username.clear()
username.send_keys("Admin")
password=driver.find_element(By.XPATH,'//input[@name="password"]')
password.clear()
password.send_keys("admin123")
login = driver.find_element(By.XPATH, "//button[@type='submit']")
login.click()
sleep(3)
print(driver.current_url)
if('dashboard' in driver.current_url):
    print("successful login")