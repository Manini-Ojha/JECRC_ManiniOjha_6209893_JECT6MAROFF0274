#go to myntra
#hover over men or women
#choose a category then click on it
#scroll to the 4th or 5th row product
#use proper waits

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver= webdriver.Chrome(options=opts)

driver.get("https://www.myntra.com/")
driver.maximize_window()
action= ActionChains(driver)

women=driver.find_element(By.XPATH,'//a[@data-group="women"]')
action.move_to_element(women).perform()

dress=driver.find_element(By.XPATH,'(//div[@class="desktop-paneContent"])[2]/descendant::li/descendant::a[text()="Dresses"]')

action.click(dress).perform()

# for i in range(4):
#     action.send_keys(Keys.PAGE_DOWN).perform()
#     sleep(3)
wait=WebDriverWait(driver,10)
# dress4=driver.find_element(By.XPATH,'(//li[@id="36930339"]')
dress4=wait.until(EC.presence_of_element_located((By.XPATH,'(//ul[@class="results-base"]/child::li[@class="product-base"])[16]')))
action.scroll_to_element(dress4).perform()
sleep(3)