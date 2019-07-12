from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('https://www.jd.com/')
    print(browser)
    input = browser.find_element_by_css_selector('#key')
    input.send_keys('Hello World!')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    print(dir(browser))
finally:
    browser.close()