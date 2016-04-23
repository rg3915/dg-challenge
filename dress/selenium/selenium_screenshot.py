import time
from selenium import webdriver

page = webdriver.Firefox()
page.maximize_window()
time.sleep(0.5)
page.get('http://localhost:8000/')
time.sleep(1)
page.save_screenshot('img/graphics.png')
page.quit()
