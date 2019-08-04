from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pdfkit
import requests
import os 
from urllib import parse

browser = webdriver.Chrome()

try:
    browser.get('https://juejin.im/post/5b94e93b5188255c672e901e')
    # browser.get('https://juejin.im/post/5d4402f4e51d4561ab2be986?utm_source=gold_browser_extension')

    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'article')))
    article = browser.find_element_by_tag_name('article')
    aa = article.get_attribute('innerHTML')
    imgs = article.find_elements_by_tag_name('img')
    # 将所有的图片下载到本地，因为掘金开启了防盗链
    # for img in imgs:
    #     img_src = img.get_attribute('data-src')
    #     if not img_src:
    #         continue
    #     response = requests.get(img_src)
    #     filename = os.path.basename(img_src)
    #     filename = img_src.split('?')[0].split('/')[-1]
    #     print(img_src)
    #     save_path = os.path.join('pic', filename)
    #     with open(save_path, 'wb') as f:
    #         response = requests.get(img_src)
    #         f.write(response.content) 
        
    # print(aa)
    # bb = aa.replace('data-src', 'src').replace(r'src="https://user-gold-cdn.xitu.io/2018/9/9/', r'src="/pic/')
    bb = aa.replace('data-src', 'src').replace(r'format/webp/ignore-error/1', r'')

    # format/webp/ignore-error/1

    with open('123.html', 'w') as f:
        f.write(bb)
    options = { 'encoding': "UTF-8" }  
    with open('123.html', 'r') as f:
        pdfkit.from_file(f, 'article2.pdf', options=options)
    # pdfkit.from_string(r'ljsflslfjslfjl<img src="http://localhost:8080/pic/165be03d7505b1af" />', 'article3.pdf', options=options)


    

finally:
    browser.close()