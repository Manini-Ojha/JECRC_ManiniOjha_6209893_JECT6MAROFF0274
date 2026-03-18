from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import (Keys)
from time import sleep

driver=webdriver.Chrome()
driver.get('https://demoqa.com/automation-practice-form')
firstName=driver.find_element(By.ID, 'firstName')
firstName.clear()
firstName.send_keys('Jane')

lastName=driver.find_element(By.ID, 'lastName')
lastName.clear()
lastName.send_keys('Doe')

email=driver.find_element(By.ID, 'userEmail')
email.clear()
email.send_keys('JaneDoe@yahoo.com')

gender=driver.find_element(By.XPATH, '//div[@class="col-md-9 col-sm-12"]/descendant::input[@id="gender-radio-2"]')
# gender.clear
gender.click()

number=driver.find_element(By.ID, 'userNumber')
number.clear()
number.send_keys('1234567890')

subjects= driver.find_element(By.ID, 'subjectsInput')
subjects.clear()
subjects.send_keys('My favorite subject')

checkbox=driver.find_element(By.XPATH, '//div[@class="col-md-9 col-sm-12"]/descendant::input[@id="gender-radio-2"]')
checkbox.click()
checkbox2=driver.find_element(By.XPATH, '//div[@class="col-md-9 col-sm-12"]/descendant::input[@id="hobbies-checkbox-3"]')
checkbox2.click()

img_upload=driver.find_element(By.ID, 'uploadPicture')
# img_upload.click()
img_upload.send_keys(r'C:\Users\Manini\Downloads\Gemini_Generated_Image_x6oyewx6oyewx6oy.png')

address=driver.find_element(By.ID, 'currentAddress')
address.clear()
address.send_keys('123 Main Street')

state_dropdown=driver.find_element(By.ID, 'react-select-3-input')
# state_dropdown.click()
state_dropdown.send_keys("Rajasthan", Keys.ENTER)

city_dropdown=driver.find_element(By.ID,'react-select-4-input')
city_dropdown.send_keys("Rajasthan", Keys.ENTER)

sleep(5)

submit = driver.find_element(By.XPATH, '//button[@id="submit"]')
# submit.click()
# sleep(2)

driver.quit()
