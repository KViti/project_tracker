from selenium import webdriver as wd

global browser
browser = wd.Chrome("/usr/bin/chromedriver/")
browser.get('https://rozetka.com.ua/')
# browser.close()
# browser.quit()