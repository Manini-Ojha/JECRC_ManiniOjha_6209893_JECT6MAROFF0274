from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

#Text field
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

name=driver.find_element(By.ID,"name")
name.clear()
name.send_keys("Manini")
sleep(5)
email=driver.find_element(By.XPATH,'//input[@placeholder="Enter EMail"]') #the xpath is called locator strategy, locator expression
email.clear()
email.send_keys("ojhamanini22@yahoo.com")
sleep(5)

print(name.get_attribute('placeholder')) #returns the value
print(email.get_attribute('value'))

#search bar
driver.get("https://www.asos.com/")
search=driver.find_element(By.ID,'chrome-search')
print(search.get_attribute('placeholder'))
print(search.get_attribute('value'))
search.clear()
search.send_keys("black dress")
print(search.get_attribute('value'))
sleep(2)

#button
search_button=driver.find_element(By.XPATH,'//button[@type="submit"]')
search_button.click()

search_button.send_keys('red dress', Keys.ENTER)

#Radio button
driver.find_element(By.ID,'female').click()

#checkbox
driver.find_element(By.XPATH,'//label[text()="Monday"]/preceding-sibling::input').click()
monday_checkbox=driver.find_element(By.XPATH,'//input[@id="monday"]/following-sibling::label')
monday_checkbox.click()
print(monday_checkbox.text()) #returns only inner text
driver.quit()