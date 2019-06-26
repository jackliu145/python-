import socket, ssl

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = ssl.wrap_socket(socket.socket())
s.connect(('www.sina.com.cn', 443))

s.send(b'GET /HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n')

buffer = []
while True:
    b = s.recv(10)
    if b:
        buffer.append(b)
    else:
        break
data = b''.join(buffer)

# print(buffer)
print(data.decode())

s.close()