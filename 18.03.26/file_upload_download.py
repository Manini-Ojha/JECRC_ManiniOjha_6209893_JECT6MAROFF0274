from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
# driver.get('https://the-internet.herokuapp.com/upload')
# driver.maximize_window()
# choose_file = driver.find_element(By.ID, 'file-upload')
# choose_file.send_keys(r'C:\Users\Manini\Downloads\Gemini_Generated_Image_x6oyewx6oyewx6oy.png')
# submit_button = driver.find_element(By.ID, 'file-submit')
# submit_button.click()
# sleep(5)

driver.get('https://the-internet.herokuapp.com/download')
driver.maximize_window()
driver.find_element(By.XPATH, '//a[text()="Gemini_Generated_Image_x6oyewx6oyewx6oy.png"]').click()
sleep(10)
print('downloaded')