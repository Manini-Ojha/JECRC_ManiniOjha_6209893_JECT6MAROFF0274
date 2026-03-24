from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver= webdriver.Chrome(options=opts)

driver.get("https://supertails.com/")
driver.maximize_window()
action= ActionChains(driver)

action.send_keys(Keys.PAGE_DOWN).perform()
sleep(3)
action.send_keys(Keys.PAGE_UP).perform()
sleep(3)
#control is to copy something
action.key_down(Keys.CONTROL).send_keys('a').perform()
#every hold should have a release
#key_down=press on
#key_up=release key
#every key_down has a key_up
sleep(3)
action.key_up(Keys.CONTROL).perform()
sleep(3)
action.key_down(Keys.CONTROL).send_keys('c').perform()
sleep(3)
action.key_up(Keys.CONTROL).perform()
# sleep(3)
# pasted=action.keys_down(Keys.CONTROL).send_keys('v')key_up(Keys.CONTROL)
# pasted.perform()
# print(pasted)

driver.get(r'C:\Users\Manini\Desktop\SeleniumForMom\23.03.2026\Address_form.html')
driver.maximize_window()

present=driver.find_element(By.ID,'presentAddress')
permanent=driver.find_element(By.ID,'permanentAddress')

present.send_keys('JECRC,JAIPUR, RJ')
sleep(3)
present.click()
action.key_down(Keys.CONTROL).send_keys('a').perform()
sleep(3)
action.key_down(Keys.CONTROL).send_keys('c').perform()
sleep(3)
permanent.click()
action.key_down(Keys.CONTROL).send_keys('v').perform()
sleep(3)

driver.get(r'C:\Users\Manini\Desktop\SeleniumForMom\23.03.2026\index1.html')
driver.maximize_window()
driver.find_element(By.ID,'password').send_keys('mani')
sleep(3)
show_pwd=driver.find_element(By.ID,'eyeBtn')
action.click_and_hold(show_pwd).perform()
sleep(3)
action.release().perform()