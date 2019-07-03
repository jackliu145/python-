import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match(r'^Hello\s\d\d\d\s\d{4}\s\w{10}', content)   # 从头开始找，开头不匹配，就不匹配了 就是说只要第一个字符不匹配整个匹配就不能成功
if result:
    print(result)
    print(result.group())
    print(result.span())
else:
    print('不匹配')

result = re.search(r'ello\s\d\d\d\s\d{4}\s\w{10}', content)  # 从头开始找，找到匹配的为止
if result:
    print(result)
    print(result.group())
    print(result.span())
else:
    print('不匹配')