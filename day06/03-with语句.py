with open('hello.log', 'r') as f:
    for line in f.readlines():  # 按行读
        print(line.strip())

# with open('read.md', 'r', -1, 'UTF-8') as f:
#     try:
#         while True:
#             size = f.read(100)
#             print(size)
#     except IOError as e:
#         pass