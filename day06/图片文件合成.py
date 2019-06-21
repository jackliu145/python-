with open('123.jpg', 'rb') as pic, open('06.rar', 'rb') as tx, open('ttt.jpg', 'wb') as tt:
    tt.write(pic.read())
    tt.write(tx.read())


    