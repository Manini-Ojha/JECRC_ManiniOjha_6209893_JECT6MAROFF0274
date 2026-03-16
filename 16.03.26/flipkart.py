#1.navigate flipkart
#2.find search field and search for a product
#3.get attribute of the product searched
#4.click on search button
#5.click on check box or boxes in filter
#6.get the text of that filter
#7.find first product
#8. find the image element
#9.print get element of src

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)


driver.get("https://www.flipkart.com/")
driver.maximize_window()
search=driver.find_element(By.XPATH,'//form[@class="lilxh_ header-form-search"]/descendant::div[@class="Afujtw"]/child::input[@placeholder="Search for Products, Brands and More"]')
search.clear()
sleep(2)
search.send_keys("lipstick", Keys.ENTER)
# search = driver.find_element(By.XPATH,'//form[@class="rcHWnF header-form-search"]/descendant::div[@class="DjsUBA"]/child::input[@title="Search for Products, Brands and More"]')
# value=search.get_attribute("value")
# print(value)
sleep(5)
# search_button=driver.find_element(By.XPATH, '//form[@class="lilxh_ header-form-search"]/child::div/child::button[@class="XFwMiH"]')
# search_button=driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
# sleep(5)
# search_button.click()
# sleep(2)
# checkbox=driver.find_element(By.XPATH,'//div[@class="Za3X8s"]/child::div[@title="NYKAA"]').click()
checkbox = driver.find_element(By.XPATH,'//div[text()="MAYBELLINE NEW YORK"]')
sleep(2)
checkbox.click()
sleep(5)
# print(checkbox.text())
img=driver.find_element(By.XPATH,'//img[@loading="eager"]')
img.get_attribute('src')


