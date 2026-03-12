#Use all methods for chrome browser

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')
driver.maximize_window()
sleep(5)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(2)

driver.close()

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
driver.get('https://www.webtoons.com/')
driver.maximize_window()

driver.quit()