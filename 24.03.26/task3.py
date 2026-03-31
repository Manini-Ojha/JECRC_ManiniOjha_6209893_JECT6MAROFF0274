from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
sleep(5)
wait = WebDriverWait(driver, 10)
parent_window = driver.current_window_handle
sleep(3)
driver.find_element(By.XPATH,'//button[@id="tabButton"]').click()
sleep(5)
driver.find_element(By.XPATH,'//button[@id="windowButton"]').click()
sleep(5)
driver.find_element(By.XPATH,'//button[@id="messageWindowButton"]').click()
sleep(5)


all_windows = driver.window_handles
print(all_windows)



driver.switch_to.window(all_windows[1])

# heading_w1=driver.find_element(By.XPATH,'//h1[@id="sampleHeading"]')
# sleep(15)
heading_w1=wait.until(EC.presence_of_element_located((By.ID,"sampleHeading")))
# heading_w1.click()

assert heading_w1.text == "This is a sample page","couldn't find what you're looking for"
sleep(5)

driver.switch_to.window(all_windows[2])
sleep(5)
# heading_w2=driver.find_element(By.XPATH,'//h1[@id="sampleHeading"]')
# sleep(8)
heading_w2=wait.until(EC.presence_of_element_located((By.ID,"sampleHeading")))
# heading_w2.click()
assert heading_w2.text == "This is a sample page","couldn't find what you're looking for"
sleep(5)
driver.switch_to.window(all_windows[3])
sleep(5)
# heading_w3=driver.find_element(By.XPATH,'//body')
# sleep(15)
# heading_w3=wait.until(EC.presence_of_element_located((By.XPATH,'//body')))
# # heading_w3.click()
# assert heading_w3.text == "Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization.","couldn't find what you're looking for"
# sleep(8)
driver.quit()