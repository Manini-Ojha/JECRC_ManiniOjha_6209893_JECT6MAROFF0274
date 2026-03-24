#action chains= related to performing mouse and keyboard actions
#hovering action
#drag and drop
#we have to import it from common

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver= webdriver.Chrome(options=opts)

driver.get("https://the-internet.herokuapp.com/drag_and_drop")
driver.maximize_window()
sleep(3)

action= ActionChains(driver)

origin_ele=driver.find_element(By.ID,'column-a')
target_ele=driver.find_element(By.ID,'column-b')

action.drag_and_drop(origin_ele,target_ele).perform() #action chains don't work without .perform

driver.get("https://supertails.com/")
driver.maximize_window()

#move_to_element performs hovering action

ele=driver.find_element(By.XPATH,'(//span[contains(text(),"Dogs")])[1]')
action.move_to_element(ele).perform()

driver.get("https://demoqa.com/droppable")
driver.maximize_window()
sleep(3)
origin_e=driver.find_element(By.ID,'draggable')
target_e=driver.find_element(By.ID,'droppable')

action.drag_and_drop(origin_e,target_e).perform()

#verification using assert
text=driver.find_element(By.XPATH,'//p[text()="Dropped!"]')
assert "Dropped!"== text.text, "I don't think the drag was successful"
print("yep! dropped!")

wait=WebDriverWait(driver,10)
prevent_prop=wait.until(EC.element_to_be_clickable((By.ID,"droppableExample-tab-preventPropogation")))
prevent_prop.click()

o_ele=wait.until(EC.visibility_of_element_located((By.ID,'dragBox')))
t_outer1_ele=wait.until(EC.visibility_of_element_located((By.XPATH,'(//p[text()="Outer droppable"])[1]')))
# t_inner1_ele=wait.until(EC.visibility_of_element_located(By.ID,'notGreedyInnerDropBox'))

action.drag_and_drop(o_ele,t_outer1_ele).perform()
# action.drag_and_drop(o_ele,t_inner1_ele).perform()



#scrolling to a particular element
driver.get("https://supertails.com/")
driver.maximize_window()

catto=driver.find_element(By.XPATH,'//div[@data-ganame="Breed 5"]')
action.scroll_to_element(catto).perform()
sleep(5)

#SCROLL TO V/S SCROLL BY
#both take pixels
#scroll to: scrolls to that target from wherever the position is of the mouse rn
#scroll by: scrolls from the position of the mouse to the next/following mentioned amount of pixels

#when you're scrolling to the top we use negative values and when scrolling down, positive values

#scroll from origin will only take positive values

action.scroll_by_amount(0,-500).perform()
sleep(5)
# action.scroll_from_origin(0,0,1000).perform()
# sleep(5)

#click->left click
#context click->right click
#double click->double click

#Keyboard actions requires importing Keys from common class