from selenium import webdriver

browsers = [webdriver.Chrome,webdriver.Edge,webdriver.Firefox]
for browser in browsers:
    driver = browser()
    driver.get('https://www.youtube.com/')
    driver.maximize_window()
    print(driver.title)
    print(driver.name)
    print(driver.current_url)
