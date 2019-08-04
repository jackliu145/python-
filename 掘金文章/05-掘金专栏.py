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
    browser.get('https://juejin.im/post/5b94e93b5188255c672e901e')
    # browser.get('https://juejin.im/post/5b037d5c518825426e024473')
    # browser.get('https://juejin.im/post/5d42f48cf265da03ab422e08')
    # browser.get('https://juejin.im/post/59e0110e6fb9a0452b483c9d')
    # browser.get('https://juejin.im/post/5d427f306fb9a06b122f1b94')


    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'article')))
    article = browser.find_element_by_tag_name('article')
    aa = article.get_attribute('innerHTML')
    title = article.find_element_by_class_name('article-title')
    bb = aa.replace('data-src', 'src').replace(r'format/webp/ignore-error/1', r'')
    options = { 'encoding': "UTF-8" }  
    print(title.text)
    pdf_name = ''.join(re.findall('[0-9A-z\u4e00-\u9fa5]', title.text))
    pdfkit.from_string(bb, pdf_name+'.pdf', options=options)

finally:
    browser.close()