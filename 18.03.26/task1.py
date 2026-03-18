from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/')
checkbox=driver.find_element(By.LINK_TEXT, 'Checkboxes')
drag=driver.find_element(By.PARTIAL_LINK_TEXT, 'Drag')
list=driver.find_elements(By.TAG_NAME, 'li')
print(len(list))
driver.get('https://the-internet.herokuapp.com/tables')
website=driver.find_element(By.XPATH, '//table[@id="table1"]/tbody[1]/tr[3]/td[text()="jdoe@hotmail.com"]/following-sibling::td[2]')
print("found")
delete=driver.find_element(By.XPATH, '//table[@id="table1"]/tbody[1]/tr[3]/td[6]/child::a[text()="delete"]')
print("found")
table2=driver.find_element(By.XPATH, '//div[@class="example"]/descendant::table[2]')
print("found")
tr=driver.find_element(By.XPATH, '//div[@class="example"]/descendant::table[2]/descendant::td[@class="dues"][3]/parent::tr')
print("found")