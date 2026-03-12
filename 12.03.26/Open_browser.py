#To open the browser
from selenium import webdriver
from time import sleep

#Chrome
driver = webdriver.Chrome() #driver is an object #opens the broswer and closes it as soon as the commands have been executed
sleep(5)

driver.get('https://supertails.com/')#broswer opens this website
driver.maximize_window()#browser window is maximized
sleep(2)

driver.back() #will show blank page again
sleep(2)

driver.forward() #will show supertails again
sleep(2)

driver.refresh() #will refresh the page
sleep(2)

driver.minimize_window()#browser window gets minimized and shows up in the task bar
sleep(2)

#Edge
# driver= webdriver.Edge()
# sleep(5)
# driver.get('https://youtube.com/')
# driver.maximize_window()
# sleep(5)
# driver.minimize_window()
# sleep(5)

#Firefox
# driver=webdriver.Firefox()
# sleep(5)
