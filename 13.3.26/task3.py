from selenium import webdriver
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://www.amazon.in/")
search=driver.find_elements(By.CSS_SELECTOR,'#twotabsearchtextbox')
logo=driver.find_elements(By.CSS_SELECTOR,'a[id="nav-logo-sprites"]')
cart=driver.find_elements(By.CSS_SELECTOR,'input[id="nav-cart"]')
signin=driver.find_elements(By.CSS_SELECTOR,'div[id="nav-link-accountList"] a[href*="https://www.amazon.in/ap/signin?"]')
anchors=driver.find_elements(By.CSS_SELECTOR,'div[id="nav-xshop"] ul[class="nav-ul"] li[class="nav-li"] div[class="nav-div"] a[href*="nav_"]')
print(len(anchors))
print("script ran successfully")
driver.quit()