import requests
import re

headers = {
    'User-Agent' : 'Molliza 5.0',
}
r = requests.get('https://www.zhihu.com/explore', headers=headers)

reg = r'<a\s+class=\"question_link\".*?>(.*?)</a>'
pattern = re.compile(reg, re.S)
titles = re.findall(pattern, r.text)
for title in titles:
    print(title)