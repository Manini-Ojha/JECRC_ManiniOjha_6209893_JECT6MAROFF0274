from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()

#simple alert
driver.find_element(By.XPATH,'//button[@id="alertButton"]').click()
sleep(3)
alert=driver.switch_to.alert
alert.accept()
sleep(3)

#simple alert
driver.find_element(By.XPATH,'//button[@id="alertButton"]').click()
sleep(10)
alert=driver.switch_to.alert
alert.accept()
sleep(3)

#confirmation alert
driver.find_element(By.XPATH,'//button[@id="confirmButton"]').click()
sleep(3)
alert=driver.switch_to.alert
alert.accept()
sleep(3)

driver.find_element(By.XPATH,'//button[@id="confirmButton"]').click()
sleep(3)
alert=driver.switch_to.alert
alert.dismiss()
sleep(3)

#prompt alert
driver.find_element(By.XPATH,'//button[@id="promtButton"]').click()
sleep(3)
alert=driver.switch_to.alert
alert.send_keys('qwerty')
sleep(3)
alert.accept()
sleep(3)


driver.find_element(By.XPATH,'//button[@id="promtButton"]').click()
sleep(3)
alert=driver.switch_to.alert
alert.send_keys('qwerty')
sleep(3)
alert.dismiss()
sleep(3)