from datetime import datetime, timedelta

now = datetime.now()

time = now + timedelta(hours = 10)   # 加上10个小时

print(time)