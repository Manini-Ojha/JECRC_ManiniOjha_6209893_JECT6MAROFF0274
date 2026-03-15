from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
sleep(2)
driver.get("https://www.circbuzz.com/")
sleep(2)
driver.get("https://www.myntra.com/")
sleep(2)



