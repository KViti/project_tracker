from selenium import webdriver
import time
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
global browser
browser = webdriver.Chrome()
browser.get('https://rozetka.com.ua/')
while (True):
    pass
# browser.close()
# browser.quit()