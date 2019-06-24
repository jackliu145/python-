import base64

h = base64.b64encode('hello'.encode())
print(h)

r = base64.b64decode(b'aGVsbG8=')
print(r)


# 请写一个能处理去掉=的base64解码函数：

def safe_base64_decode(s):
    left = len(s) % 4
    if left != 0:
        for x in range(left):
            s += b'='
    return base64.b64decode(s)
# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')