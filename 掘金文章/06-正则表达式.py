import re

# reg =re.compile(r'[0-9A-Za-Z\u4e00-\u9fa5]')
a = re.findall('[0-9A-z\u4e00-\u9fa5]', 'flsjHf?:中文')
print(a)