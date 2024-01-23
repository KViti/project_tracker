from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By

link = "https://yandex.ru/images/"
browser = webdriver.Chrome()
browser.get(link)
# serch_string = browser.find_element(By.XPATH, "")
