# 1. navigate to amazon
# 2. search a product through send_keys
# BUT don't click on search or keys.enter
# 3. Wait for the suggestions to appear
# 4. Click on 4th suggestion
# 5. Click on Sort By and click on newest
# 6. Click on free shipping check box
# 7. wait for first product and return me the name=price
# (without using inner text)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.amazon.in/")
driver.maximize_window()

wait=WebDriverWait(driver,15)

search=wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@class="nav-search-field "]/child::input')))
search.send_keys("tshirt for women")
search_on=wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@class="two-pane-results-container"]/descendant::div[@id="sac-suggestion-row-4"]')))
search_on.click()

sort=wait.until(EC.element_to_be_clickable((By.XPATH,'//span[@class="a-button-text a-declarative"]')))
sort.click()
sort_by=wait.until(EC.visibility_of_element_located((By.XPATH,'(//ul[@class="a-nostyle a-list-link"]/descendant::a[@tabindex="0"])[5]')))
sort_by.click()

free_ship=wait.until(EC.visibility_of_element_located((By.XPATH,'(//i[@class="a-icon a-icon-checkbox"])[3]')))
free_ship.click()

name=wait.until(EC.visibility_of_element_located((By.XPATH,'(//div[@data-cy="title-recipe"]/descendant::span)[1]')))
price=wait.until(EC.visibility_of_element_located((By.XPATH,'(//span[@class="a-price"])[1]')))
print(f'{name.text} = {price.text}')
