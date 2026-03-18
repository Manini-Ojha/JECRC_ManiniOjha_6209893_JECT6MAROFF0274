from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

#How to use Assert?
#Assert is a keyword in Python which checks if a statement is true or false, if it's true then it continues and if false then it throws an assertion error


driver.get("https://www.lenskart.com/")
driver.maximize_window()
sleep(5)

eye=driver.find_element(By.ID,'lrd1')
print(eye.text)

#asert TRUECONDITION, ASSERTIONERRORPRINT
assert 'EYEGLASSES' in eye.text, 'did not find EYEGLASSES text'
print('success')

# assert 'GLASSES' == eye.text, 'did not find EYEGLASSES text'
# print('success')

driver.get("https://www.myntra.com//")
sleep(5)
kids=driver.find_element(By.XPATH,'//div[@class="desktop-navContent"]/descendant::a[@data-reactid="335"]')
print(kids.text)
assert 'KIDS' in kids.text, 'did not find KIDS text'
print('success')

driver.get("https://www.lenskart.com/vincent-chase-vc-e16668-c2-eyeglasses.html")
sleep(5)
check=driver.find_element(By.XPATH,'//button[@data-cy="Clarity-Box-Button"]')
print(check.text)
assert 'Check' in check.text, 'did not find Check text'
print(check.is_enabled())
check.click()
sleep(5)
pincode=driver.find_element(By.TAG_NAME,'input')
check1=driver.find_element(By.XPATH,'//div[@data-cy="check-enterd-pincode"]')
# print(pincode.text)
print(check1.is_enabled())
pincode.send_keys('123456')
if check1.is_enabled():
    check1.click()
    print('success')

#func + f8 in sources will help you find the loading element(ajax spinners) in the elements, to resume, go to sources again and click fun +f8 again
driver.quit()
