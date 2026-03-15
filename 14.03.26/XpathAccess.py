from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
#XPATH ACCESS

#Ancestor
div=driver.find_elements(By.XPATH, '//span[text()="All"]/ancestor::div[@id="nav-main"]')
seeMore=driver.find_elements(By.XPATH, '//span[@class="a-truncate"]/ancestor::div[@class="_Zmx1a_fluidQuadImageLabelBody_3tld0"]')

#Descendant
InnerText=driver.find_elements(By.XPATH, '//div[@id="nav-main"]/descendant::span[text()="All"]')


#Siblings
Sibling=driver.find_elements(By.XPATH, '//a[text()="Fresh"]/ancestor::li/following-sibling::li[1]')
#since there were a lot of siblings of li but each sibling leads to a single element, we can simply mention the index and we'll reach our element