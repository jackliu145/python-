from datetime import datetime

print(datetime.now())  # 当前日期

time = datetime(1971, 1, 1)

print(time)
print(time.timestamp())   #时间戳

print(isinstance(time.now(), datetime))   


t = 11507200.0
print(datetime.fromtimestamp(t))

#时间格式化
#字符串转换为datetime
datestr = '2019-12-11'

date = datetime.strptime(datestr, '%Y-%m-%d')
print(date)

#datetime转换为字符串
t = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M')
print(t)
