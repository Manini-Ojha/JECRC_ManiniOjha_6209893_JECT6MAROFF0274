from selenium import webdriver
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')

#locators
#1. HTML elements

# #id
# id_name1=driver.find_element(By.ID,'colors')
# print(f'The id was found')
# id_name2=driver.find_element(By.ID,'header')
# print(f'The id was found')
# id_name3=driver.find_element(By.ID,'Header1')
# print(f'The id was found')
# id_name4=driver.find_element(By.ID,'main')
# print(f'The id was found')
# id_name5=driver.find_element(By.ID,'crosscol')
# print(f'The id was found')
#
#
# #class
# class_name1=driver.find_elements(By.CLASS_NAME,'form-check-input')
# print(f'The class name was found')
# class_name2=driver.find_elements(By.CLASS_NAME,'cap-top')
# print(f'The class name was found')
# class_name3=driver.find_elements(By.CLASS_NAME,'cap-left')
# print(f'The class name was found')
# class_name4=driver.find_elements(By.CLASS_NAME,'content')
# print(f'The class name was found')
# class_name5=driver.find_elements(By.CLASS_NAME,'content-inner')
# print(f'The class name was found')
#
#
# #name
# name_name1=driver.find_element(By.NAME,'Navbar')
# print(f'The name was found')
# name_name2=driver.find_element(By.NAME,'Header')
# print(f'The name was found')
# name_name3=driver.find_element(By.NAME,'Cross-Column')
# print(f'The name was found')
# name_name4=driver.find_element(By.NAME,'Main')
# print(f'The name was found')
# name_name5=driver.find_element(By.NAME,'animals')
# print(f'The name was found')
#
#
# #tag
# tag_name1=driver.find_elements(By.TAG_NAME,'a')
# print(f'The tag name was found')
# tag_name2=driver.find_elements(By.TAG_NAME,'select')
# print(f'The tag name was found')
# tag_name3=driver.find_elements(By.TAG_NAME,'input')
# print(f'The tag name was found')
# tag_name4=driver.find_elements(By.TAG_NAME,'span')
# print(f'The tag name was found')
# tag_name5=driver.find_elements(By.TAG_NAME,'div')
# print(f'The tag name was found')

#2. CSS Selectors

# name=driver.find_elements(By.CSS_SELECTOR,'select[id="animals"]')
# name=driver.find_elements(By.CSS_SELECTOR,'#animals')
# #will find only first occurrence when we use find_element
# anchor=driver.find_elements(By.CSS_SELECTOR,'a[href*="testautomationpractice"]')
# #the * after href indicates a substring
# anchor2=driver.find_elements(By.CSS_SELECTOR,'a[href^="https://"]')
# #the ^ after href is for the starting substring of a string
# anchor3=driver.find_elements(By.CSS_SELECTOR,'a[href$=".com"]')
#the $ symbol indicates the ending substring of a string

##DRAWBACK FOR CSS SELECTOR: 1.it only traverses from top to bottom 2.Can't find inner text
#hard to target a particular element:

#using tag_names
#attr1= driver.find_elements(By.CSS_SELECTOR,'div[class="widget-content"] a[href=["testautomationpractice.blogpost"]]')

#using 2 selectors:
#attr2=driver.find_elements(By.CSS_SELECTOR,'input[type="text"][class="register"]')

#Xpath: x= xml
#it is better than css selectors because it is powerful and efficient
#can travel all directions
#we can find elements using inner text
#slower than css selectors
#not in a readable form

#two types: absolute xpath and relative xpath, we'll be using relative xpath tho
#syntax: /html   @id,@class,@type(@attribute_name)
# <html>
#     <body>
#         <div>
#             <input id='name'>

#absolute xpath: /html/body/div/input[@id='name]
#relative xpath: //input[@id='name']

# how to do indexing in xpath?
#(//input[@id='name'])[1]

#using attributes other than id and classname to locate elements(for multiple elements being returned, use indexing to choose one, indexing starts from 1 here)
placeholder=driver.find_elements(By.XPATH,'//input[@placeholder="Enter Name"]')
for_=driver.find_elements(By.XPATH,'(//label[@for="textbox"])[1]')
type=driver.find_elements(By.XPATH,'(//input[@type="radio"])[2]')
value=driver.find_elements(By.XPATH,'//input[@value="female"]')
option=driver.find_elements(By.XPATH,'(//option[@value="white"])')
div=driver.find_elements(By.XPATH,'//div[@itemscope="itemscope"]')

#Xpath for inner text
#//a[text()="Home"]
#when we write the inner text here, we have to use complete inner text, if there are 10 lines, we have to write all 10 lines in quotes

Home=driver.find_elements(By.XPATH,'//a[text()="Home"]')
gui=driver.find_elements(By.XPATH,'//a[text()="GUI Elements"]')
pages=driver.find_elements(By.XPATH,'//a[text()="2"]')

#//a[contains(text(),"Japan")]

Japan=driver.find_elements(By.XPATH,'//option[contains(text(),"Japan")]')
Aman=driver.find_elements(By.XPATH,'//td[text()="Aman"]')
click=driver.find_elements(By.XPATH,'//h2[text()="Double Click"]')

print('worked fine')
driver.quit()