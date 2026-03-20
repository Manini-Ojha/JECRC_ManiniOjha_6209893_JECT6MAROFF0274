from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get("https://qavbox.github.io/demo/signup/")
driver.maximize_window()

wait=WebDriverWait(driver,10)

username=wait.until(EC.visibility_of_element_located((By.ID,'username')))
username.send_keys("Jane Doe")

email=wait.until(EC.visibility_of_element_located((By.ID,'email')))
email.send_keys("some@yahoo.com")

tel=wait.until(EC.visibility_of_element_located((By.ID,'tel')))
tel.send_keys("1234567691")

# fax=wait.until(EC.visibility_of_element_located((By.ID,'fax')))
# fax.send_keys("123456789")

upload=wait.until(EC.element_to_be_clickable((By.NAME,'datafile')))
upload.send_keys(r'C:\Users\Manini\Downloads\Gemini_Generated_Image_x6oyewx6oyewx6oy.png')

gender=wait.until(EC.element_to_be_clickable((By.NAME,'sgender')))
select=Select(gender)
select.select_by_value('female')

exp=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@value="one"]')))
exp.click()

skills1=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@value="automationtesting"]')))
skills1.click()

skills2=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@value="testng"]')))
skills2.click()

automation=wait.until(EC.visibility_of_element_located((By.ID,'tools')))
select1=Select(automation)
select1.select_by_index(1)
automation.click()

submit=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@id="submit"]')))
submit.click()