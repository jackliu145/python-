from lxml import etree

html = etree.parse(r'test.html', etree.HTMLParser())
result = etree.tostring(html)   # 会格式化文档
print(result.decode('utf8'))

# 获取所有节点
nodes = html.xpath('//*')
print(nodes)

# 子节点 
a = html.xpath('//li/a')
print(a)

# 孙子节点
a = html.xpath('//ul//a')
print(a)

# 父节点
item_1 = html.xpath(r'//a[@href="link4.html"]/../@class')
print(item_1)

#属性匹配
item_0 = html.xpath(r'//li[@class="item-0"]')
print(item_0)

# 内容获取
item_0_text = html.xpath(r'//li[@class="item-0"]/a/text()')
print(item_0_text)

# 属性获取
href = html.xpath('//li/a/@href')
print(href)

