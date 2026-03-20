from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get("https://abc.com/")
driver.maximize_window()

wait_obj=WebDriverWait(driver,10)

loading_circles=wait_obj.until(EC.invisibility_of_element_located((By.ID,"preloader-animated_svg__svg3")))     #this is like sleep

title_abc=driver.find_element(By.XPATH,'//span[text()="ABC SHOWS, SPECIALS & MORE"]')

assert 'SPECIALS' in title_abc.text,  "text not present"    #assert is part of python so it can't be used to find element

print('working fine')

driver.get("https://demoqa.com/dynamic-properties")
driver.maximize_window()

wait=WebDriverWait(driver,6)
enabled_before=driver.find_element(By.ID,'enableAfter')
print(enabled_before.is_enabled())

enable_btn=wait.until(EC.element_to_be_clickable((By.ID,'enableAfter')))

if enabled_before.is_enabled():
    enable_btn.click()
    print(enable_btn.text)

vis_ele=wait.until(EC.visibility_of_element_located((By.ID,'visibleAfter')))
vis_ele.click()


driver.quit()