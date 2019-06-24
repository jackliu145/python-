import re

r = re.match(r'^a\d+(\.dat$)', 'a123.dat')
print(r)
print(dir(r))