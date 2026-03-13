from selenium import webdriver
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://the-internet.herokuapp.com/login')
username=driver.find_element(By.XPATH,'//input[@name="username"]')
password=driver.find_element(By.XPATH,'//input[@id="password"]')
login=driver.find_element(By.XPATH,'//button[@type="submit"]')
link=driver.find_element(By.XPATH,'//a[text()="Elemental Selenium"]')
heading=driver.find_element(By.XPATH,'//h2[contains(text(),"Login Page")]')
print("Script ran successfully")
driver.quit()