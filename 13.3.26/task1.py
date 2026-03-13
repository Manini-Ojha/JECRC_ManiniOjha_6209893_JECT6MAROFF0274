from selenium import webdriver
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://www.cricbuzz.com/')

#html locators
id=driver.find_element(By.ID,'main-header')
class_name=driver.find_elements(By.CLASS_NAME,'min-h-container')
name=driver.find_elements(By.NAME,'google_ads_iframe_/1024780/Desktop_new/LB_0')
tag=driver.find_elements(By.TAG_NAME,'a[href*="cricket-series"]')

#css selectors
class_name2=driver.find_elements(By.CSS_SELECTOR,'.min-h-container')
id_name=driver.find_element(By.CSS_SELECTOR,'#leaderboard')
title=driver.find_elements(By.CSS_SELECTOR,'a[title="Go add-free"]')

#XPath
element1=driver.find_elements(By.XPATH,'/html/body/div/div[2]')
element2=driver.find_elements(By.XPATH,'//div[div[@class="w-full text-white bg-[#4a4a4a] text-xs dark:bg-cbHdrBkgDark flex justify-between items-center h-10 relative"]]')
liveScores=driver.find_elements(By.XPATH,'//a[text()="Live Scores"]')
News=driver.find_elements(By.XPATH,'//a[contains(text(),"News")]')

print("Script has been executed successfully")
driver.quit()