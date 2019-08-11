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
    url = 'https://juejin.im/post/5b737671518825612a227e91'
    browser.get(url)
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