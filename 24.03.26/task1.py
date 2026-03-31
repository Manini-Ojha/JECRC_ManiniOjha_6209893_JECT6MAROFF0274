from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://codepen.io/gdw96/pen/jOypoYL")
driver.maximize_window()
sleep(2)

actions = ActionChains(driver)

iframe=driver.find_element(By.XPATH,'//iframe[@id="result"]')
driver.switch_to.frame(iframe)
sleep(2)
driver.find_element(By.XPATH,'//input[@id="password"]').send_keys("psswd123")
sleep(2)
show_pw=driver.find_element(By.XPATH,'//button[@id="showPsswd"]')
actions.click_and_hold(show_pw).perform()
sleep(2)
actions.release().perform()
register=driver.find_element(By.XPATH,'//div[@class="form-control center"]/child::input')
register.click()
sleep(5)
driver.switch_to.default_content()
# driver.refresh()
# sleep(5)
driver.back()
# iframe=driver.find_element(By.XPATH,'//iframe[@id="result"]')
sleep(5)

driver.switch_to.frame(iframe)
form_title=driver.find_element(By.XPATH,'//h1[text()="Registration"]')

assert 'Registration' in form_title.text, "heading of form not found"
print("heading of form has been validated")