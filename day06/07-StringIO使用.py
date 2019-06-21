from io import StringIO

s = StringIO('')
s.write('h')
s.write('ffff')

print(s.getvalue())