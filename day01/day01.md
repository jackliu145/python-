#	day01

	##	解释器

python解释器：

​	python是一种解释性语言，只要安装Python解释器，就能执行py程序。python官方提供的解释器是cpython。



##	第一个案例

```python
print('hello world!')
print('hello', 'world!')
```



##	数据类型

- 整数 (没有范围限制，无限大)

- 浮点数(同上)

- 字符串：单引号或者双引号、三个引号包起来的

  - 转义字符：'\n'。

    ```python
    print('hello\n')
    ```

    

  - r开头的字符串'\n' 表示字符不转义

    ```python
    print(r'\n')
    ```

    

  - 三个引号使用表示多行字符串。按下回车键后，下一行的开头使用...

    ```python
    print('''hello
    ... hello
    ... hllo
    ... ''');
    ```

  - b引号前开头的字符串,代表字符串中是bytes

    ```python
    '中文'.encode('utf8') #打印对应的bytes  b'\xe4\xb8\xad\xe6\x96\x87'
     b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf8') # '中文'
    ```

    

-  布尔型

  - True
  - False

- 空值

  - None

## 注释

语句前加上#代表注释

```python
print('hello world!') #这是注释
```

##	字符编码

Python3中，字符串是以Unicode编码的。

获取某个字符的Unicode整数值，获取整数对应的编码字符。

```python
num = ord('中')
print(num)  # 20013
print(chr(20013))   # 中
'中文'.encode('utf8') #打印对应的bytes  
```

#	字符串格式化

使用%s， %d 做占位符，使用%连接参数。

```python
print('hello, %s' % 'jack')   # hello, jack   
print('hello, %s, %d' % ('jack', 100))  # %后面按顺序来
```

#	List类型

List是Python的内置类型，是一种有序的集合，可以随时添加和删除其中的元素

```Python
students = ['jack', 'Mark', 'Marry']
students[0] # 'jack'

len(students)  # 3
students[3]  # IndexError

students.append('hello') # list末尾追加一个元素
studnets.insert(1, 'Tom') #将元素插入到指定索引处
students.pop() # 删除末尾的元素
students.pop(0) # 删除索引为0的元素

```

