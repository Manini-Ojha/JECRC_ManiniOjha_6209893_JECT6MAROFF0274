from nltk.sem.chat80 import country
from selenium import webdriver
from time import sleep
#the three classes we import from common are:

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.select import Select
#dropdowns are always in select tag so you need to import select class
driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com')

#we use maximize window so that elements don't overlap
driver.maximize_window()

country_dropdown=driver.find_element(By.ID,'country')
dropdown = Select(country_dropdown)

dropdown.select_by_value('australia')
sleep(2)
dropdown.select_by_index(3) #only takes int, here indexing starts from zero
sleep(2)
dropdown.select_by_visible_text('United Kingdom')

#1. go to lenskart
#2. search a product
#3. go to dropdown and select Biggest Savings
#4. find the innertext of the first product

driver.get('https://www.lenskart.com/')
search=driver.find_element(By.XPATH,'//input[@id="autocomplete-0-input"]')
search.clear()
search.send_keys('sunglasses',Keys.ENTER)
sleep(2)
filter=driver.find_element(By.XPATH,'//select[@id="sortByDropdown"]')
sleep(2)
sort=Select(filter)
sort.select_by_value('saving')

first_element=driver.find_element(By.XPATH,'(//p[@class="sc-23b7d3eb-2 dQrJBg"])[1]')
print(first_element.text)

driver.quit()