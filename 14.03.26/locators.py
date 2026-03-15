from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()

#Link Text
driver.get("https://www.testautomationpractice.blogpost.com/")
Courses=driver.find_elements(By.LINK_TEXT, "Udemy Courses")
Udemy=driver.find_elements(By.PARTIAL_LINK_TEXT, "Udemy")

Price=driver.find_elements(By.XPATH, '//td[text()="Learn Java"]/following-sibling::td[3]')
Selenium=driver.find_elements(By.XPATH, '//td[text()="Amod"]/ancestor::table[@name="BookTable"]')
Books=driver.find_elements(By.XPATH, '//td[text()="300"]/preceding-sibling::td[3]')
Names=driver.find_elements(By.XPATH,'//tbody[@id="rows"]/descendant::tr/descendant::td[1]')