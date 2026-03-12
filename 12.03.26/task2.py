from pydoc import browse

from selenium import webdriver
from time import sleep
browsers=[webdriver.Chrome,webdriver.Edge,webdriver.Firefox]
for browser in browsers:
    driver = browser()
    sleep(2)