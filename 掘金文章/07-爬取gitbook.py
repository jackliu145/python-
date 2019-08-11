from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pdfkit
import requests
import os 
from urllib import parse
import re

browser = webdriver.Chrome()

try:

    url = 'https://lingcoder.github.io/OnJava8/#/README'
    browser.get(url)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'active')))
    # print(browser.page_source)
    category = browser.find_element_by_class_name('sidebar-nav')
    aa = category.get_attribute('innerHTML')
    # print(aa)
    titles = category.find_elements_by_tag_name('a')
    print(titles)
    options = { 'encoding': "UTF-8" } 
    # for title in titles:
        # print(title.get_attribute('href')) 
    hh = [title.get_attribute('href') for title in titles]
    # pdf_name = ''.join(re.findall('[0-9A-z\u4e00-\u9fa5]', title.text))
    # pdfkit.from_string(bb, pdf_name+'.pdf', options=options)
    pdfkit.from_url(hh, 'hello.pdf')

finally:
    browser.close()

