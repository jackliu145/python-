import socket, threading

def handle_tcp(sock, addr):
    print('handle tcp request from %s:%s' % addr)
    sock.send(b'Welcome')
    while True:
        b = sock.recv(1024)
        if not b or b.decode('utf') == 'exit':
            break
        sock.send(('hello %s' % b.decode('utf8')).encode('utf8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))

s.listen(5)

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=handle_tcp, args=(sock, addr))
    t.start()

