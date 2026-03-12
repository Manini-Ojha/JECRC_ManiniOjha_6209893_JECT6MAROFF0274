from selenium import webdriver
#Chrome
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)
driver.get('https://supertails.com/')
driver.maximize_window()

print(f'Title is: {driver.title}')
print(f'Driver is: {driver.name}')
print(f'URL: {driver.current_url}')


#Edge
# opts = webdriver.EdgeOptions()
# opts.add_experimental_option('detach', True)
# driver=webdriver.Edge(options=opts)
# driver.get('https://supertails.com/')
# driver.maximize_window()

#Firefox
# opts = webdriver.FirefoxOptions()
# # opts.add_argument('detach') #firefox by default stays detached anyway
# driver = webdriver.Firefox(options=opts)
# driver.get('https://supertails.com/')
# driver.maximize_window()

# driver.close()
driver.quit()
