#add songs that have the words
#girl
#or
#love
#in the playlist\
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get(r'C:\Users\Manini\Desktop\RobotPythonProject\20.03.26\playlist.html')
driver.maximize_window()

songs_list=driver.find_element(By.ID,"songs")
select=Select(songs_list)

if select.is_multiple:
    for i in select.options:
        if 'Girl' in i.text :
            select.select_by_visible_text(i.text)

#list comprehension
print([i.text for i in select.all_selected_options])
# print([i.text for i in select.options])
driver.find_element(By.XPATH,"//button[text()='Add to Playlist']").click()

sleep(3)
driver.quit()