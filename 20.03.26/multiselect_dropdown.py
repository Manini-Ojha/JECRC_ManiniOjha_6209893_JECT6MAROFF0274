from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

multi_drop=driver.find_element(By.ID,"colors")
select=Select(multi_drop)

if select.is_multiple:
    select.select_by_index(3)
    select.select_by_value("blue")
    select.select_by_visible_text("Green")
print('before deselect:',[i.text for i in select.all_selected_options])
sleep(3)
select.deselect_by_value("blue")
print('after deselect:',[i.text for i in select.all_selected_options])

##driver.get() works on pdf and docs too, pdf will open and you'll only be able to read it, the docs will get downloaded and you'll have to open it in file explorer which is why we don't use it with them much

driver.get(r'C:\Users\Manini\Desktop\RobotPythonProject\20.03.26\playlist.html')
driver.maximize_window()

songs_list=driver.find_element(By.ID,"songs")
select=Select(songs_list)

if select.is_multiple:
    select.select_by_index(4)
    select.select_by_visible_text("Animals")
    select.select_by_visible_text("Shape of You")

#list comprehension
print([i.text for i in select.all_selected_options])
print([i.text for i in select.options])
driver.find_element(By.XPATH,"//button[text()='Add to Playlist']").click()

sleep(3)
driver.quit()