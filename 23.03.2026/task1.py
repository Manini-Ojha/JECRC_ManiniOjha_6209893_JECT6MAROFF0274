from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver= webdriver.Chrome(options=opts)

driver.get("https://www.wplt20.com/teams/royal-challengers-bengaluru-3513/squad")
driver.maximize_window()
action=ActionChains(driver)

# wait = WebDriverWait(driver, 10)
# player=wait.until(EC.visibility_of_element_located((By.XPATH,'//a[@data-name="Lauren Bell"]')))
# action.scroll_to_element(player).perform()
# action.send_keys(Keys.PAGE_UP).perform()

player=driver.find_element(By.XPATH,'//a[@data-name="Lauren Bell"]')
sleep(3)
action.scroll_to_element(player).perform()
sleep(3)
for i in range(4):
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(3)
