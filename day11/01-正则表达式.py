import re

str1 = 'abc123def'
reg = r'\d+'

result = re.match(reg, str1)   # 该方法值 测试字符串是否匹配
print(result)

result2 = re.findall(reg, str1)  # 查找
print(result2)

result3 = re.finditer(reg, str1)
print(result3)
for x in result3:
    print(x)